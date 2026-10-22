#!/usr/bin/env python3
"""Copy skills to a project or personal Claude Code directory without overwriting."""

import argparse
from pathlib import Path
import shutil
import sys

if __package__:
    from .validate_skills import validate_library
else:
    from validate_skills import validate_library


def install_skills(source, destination, names=None, dry_run=False):
    source, destination = Path(source), Path(destination)
    available, errors = validate_library(source)
    if errors:
        raise ValueError("Invalid source library:\n" + "\n".join(errors))
    selected = sorted(set(available if names is None else names))
    if not selected:
        raise ValueError("Select at least one skill")
    unknown = set(selected) - set(available)
    if unknown:
        raise ValueError("Unknown skills: " + ", ".join(sorted(unknown)))
    if destination.is_symlink() or destination.parent.is_symlink():
        raise ValueError("Refusing a symlinked .claude or skills destination")
    if destination.exists() and not destination.is_dir():
        raise ValueError("Destination must be a directory")
    conflicts = [name for name in selected
                 if (destination / name).exists() or (destination / name).is_symlink()]
    if conflicts:
        raise ValueError("Existing skills would be overwritten; no files copied: " + ", ".join(conflicts))
    if dry_run:
        return selected
    destination.mkdir(parents=True, exist_ok=True)
    for name in selected:
        # copytree refuses existing targets, including a collision after preflight.
        shutil.copytree(source / name, destination / name,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo"))
    return selected


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--project", type=Path, help="Install under PROJECT/.claude/skills.")
    destination.add_argument("--personal", action="store_true", help="Install under ~/.claude/skills.")
    parser.add_argument("--skill", action="append", dest="names", help="Install one named skill; repeat to select several.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print the plan without writing files.")
    args = parser.parse_args(argv)
    source = Path(__file__).resolve().parents[1] / ".claude" / "skills"
    target = (Path.home() if args.personal else args.project.expanduser().resolve()) / ".claude" / "skills"
    try:
        selected = install_skills(source, target, args.names, args.dry_run)
    except (OSError, ValueError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        return 1
    print(f"{'Would install' if args.dry_run else 'Installed'} {len(selected)} skills in {target}:")
    for name in selected:
        print(f"  {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
