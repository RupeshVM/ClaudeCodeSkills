from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_skills import install_skills
from validate_skills import parse_frontmatter, validate_library


def make_skill(root, name="example"):
    skill = root / name
    (skill / "references").mkdir(parents=True)
    (skill / "references" / "template.md").write_text("# Template\n\nUseful source material.\n", encoding="utf-8")
    (skill / "SKILL.md").write_text(
        f'---\nname: {name}\ndescription: A specific test workflow for library tooling.\n'
        'argument-hint: "[request]"\n---\n\n# Example workflow\n\n'
        'Inspect the supplied context and identify the requested deliverable. '
        'Use [the template](references/template.md) and report observed results '
        'separately from assumptions.\n', encoding="utf-8")
    return skill


class LibraryFixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.skill = make_skill(self.source)
        self.destination = self.root / "project/.claude/skills"


class ValidatorTests(LibraryFixture):
    def test_valid_skill_and_bundled_resource(self):
        self.assertEqual(validate_library(self.source), (["example"], []))

    def test_missing_required_field(self):
        with self.assertRaisesRegex(ValueError, "missing required field"):
            parse_frontmatter("---\nname: example\n---\n# Example")

    def test_rejects_duplicate_fields_and_unterminated_header(self):
        with self.assertRaisesRegex(ValueError, "duplicate field"):
            parse_frontmatter("---\nname: example\nname: other\ndescription: Text\n---")
        with self.assertRaisesRegex(ValueError, "closing"):
            parse_frontmatter("---\nname: example")

    def test_rejects_nonstrings_or_invalid_plain_yaml_text(self):
        for value in ("null", "123", "# comment", "- item", "? item", "broken:",
                      "True", "yes", "~", "2026-10-22", "[one, two]", "text # comment"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_frontmatter(f"---\nname: example\ndescription: {value}\n---")

    def test_quoted_text_and_booleans_are_preserved(self):
        fields, _ = parse_frontmatter(
            '---\nname: example\ndescription: "123: a literal description"\n'
            "argument-hint: 'a user''s request'\ndisable-model-invocation: true\n---")
        self.assertEqual(fields["description"], "123: a literal description")
        self.assertEqual(fields["argument-hint"], "a user's request")
        self.assertIs(fields["disable-model-invocation"], True)

    def test_rejects_quoted_boolean_and_invalid_quote_escaping(self):
        for extra in ('disable-model-invocation: "true"', "argument-hint: 'a'''b'"):
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                parse_frontmatter(f"---\nname: example\ndescription: Text\n{extra}\n---")

    def test_name_must_match_directory(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text().replace("name: example", "name: another"))
        self.assertTrue(any("match its directory" in error for error in validate_library(self.source)[1]))

    def test_missing_resource_is_reported(self):
        (self.skill / "references/template.md").unlink()
        self.assertTrue(any("missing linked resource" in error for error in validate_library(self.source)[1]))

    def test_resources_cannot_escape_the_installed_skill(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text().replace("references/template.md", "../outside.md"))
        self.assertTrue(any("escapes its skill" in error for error in validate_library(self.source)[1]))

    def test_symlinked_resource_is_rejected(self):
        target = self.root / "outside.md"
        target.write_text("External data")
        (self.skill / "references/linked.md").symlink_to(target)
        self.assertTrue(any("symlinked resource" in error for error in validate_library(self.source)[1]))

    def test_empty_library_and_missing_skill_file_fail(self):
        self.assertTrue(validate_library(self.root / "missing")[1])
        (self.skill / "SKILL.md").unlink()
        self.assertTrue(any("missing SKILL.md" in error for error in validate_library(self.source)[1]))


class InstallerTests(LibraryFixture):
    def test_copies_complete_skill_and_resources(self):
        self.assertEqual(install_skills(self.source, self.destination), ["example"])
        self.assertEqual((self.destination / "example/SKILL.md").read_bytes(), (self.skill / "SKILL.md").read_bytes())
        self.assertTrue((self.destination / "example/references/template.md").is_file())
        self.assertEqual(validate_library(self.destination), (["example"], []))

    def test_selective_installation(self):
        make_skill(self.source, "second")
        install_skills(self.source, self.destination, ["second"])
        self.assertTrue((self.destination / "second/SKILL.md").is_file())
        self.assertFalse((self.destination / "example").exists())

    def test_dry_run_does_not_create_destination(self):
        self.assertEqual(install_skills(self.source, self.destination, dry_run=True), ["example"])
        self.assertFalse(self.destination.parent.exists())

    def test_collision_preserves_existing_files_and_copies_nothing(self):
        make_skill(self.source, "second")
        existing = self.destination / "second"
        existing.mkdir(parents=True)
        sentinel = existing / "custom.md"
        sentinel.write_text("User changes")
        with self.assertRaisesRegex(ValueError, "no files copied"):
            install_skills(self.source, self.destination)
        self.assertEqual(sentinel.read_text(), "User changes")
        self.assertFalse((self.destination / "example").exists())

    def test_unknown_or_empty_selection_copies_nothing(self):
        for selection in (["unknown"], []):
            with self.subTest(selection=selection), self.assertRaises(ValueError):
                install_skills(self.source, self.destination, selection)
        self.assertFalse(self.destination.exists())

    def test_invalid_source_is_not_installed(self):
        (self.skill / "references/template.md").unlink()
        with self.assertRaisesRegex(ValueError, "Invalid source"):
            install_skills(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_symlinked_destination_does_not_write_outside_project(self):
        outside = self.root / "outside"
        outside.mkdir()
        self.destination.parent.parent.mkdir(parents=True)
        self.destination.parent.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlinked"):
            install_skills(self.source, self.destination)
        self.assertEqual(list(outside.iterdir()), [])

    def test_file_destination_is_rejected(self):
        self.destination.parent.mkdir(parents=True)
        self.destination.write_text("Preserve me")
        with self.assertRaisesRegex(ValueError, "directory"):
            install_skills(self.source, self.destination)
        self.assertEqual(self.destination.read_text(), "Preserve me")

    def test_generated_bytecode_is_not_installed(self):
        cache = self.skill / "__pycache__"
        cache.mkdir()
        (cache / "helper.pyc").write_bytes(b"generated")
        install_skills(self.source, self.destination)
        self.assertFalse((self.destination / "example/__pycache__").exists())

    def test_cli_installs_real_library_from_another_working_directory(self):
        project = self.root / "real-project"
        run = subprocess.run([sys.executable, str(ROOT / "scripts/install_skills.py"),
                              "--project", str(project)], cwd=self.root, text=True,
                             capture_output=True, check=True)
        original_names, errors = validate_library(ROOT / ".claude/skills")
        self.assertEqual(errors, [])
        installed_names, errors = validate_library(project / ".claude/skills")
        self.assertEqual(errors, [])
        self.assertEqual(installed_names, original_names)
        self.assertIn(f"Installed {len(original_names)} skills", run.stdout)
        subprocess.run([sys.executable, str(ROOT / "scripts/validate_skills.py"),
                        "--root", str(project)], cwd=self.root, text=True,
                       capture_output=True, check=True)


if __name__ == "__main__":
    unittest.main()
