#!/usr/bin/env python3
"""Validate this library's deliberately small, flat skill frontmatter and links.

No YAML package is needed. Supported metadata values are single-line plain,
JSON-quoted, or YAML single-quoted strings and lowercase booleans. Extend this
validator before introducing other YAML features; it is not a general YAML parser.
"""

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIELD = re.compile(r"([a-z][a-z0-9-]*):[ \t]*(.*)\Z")
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
TEXT_FIELDS = {"name", "description", "argument-hint", "model", "context", "agent"}
BOOL_FIELDS = {"disable-model-invocation", "user-invocable"}


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("must start with a --- frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("missing closing frontmatter delimiter") from None
    metadata = {}
    for line in lines[1:end]:
        if not line.strip() or line.startswith("#"):
            continue
        match = FIELD.fullmatch(line)
        if not match:
            raise ValueError("frontmatter must use flat, single-line scalar fields")
        key, raw = match.groups()
        if key in metadata:
            raise ValueError(f"duplicate field: {key}")
        if not raw:
            raise ValueError(f"empty value: {key}")
        if raw.startswith('"'):
            try:
                value = json.loads(raw)
            except json.JSONDecodeError as error:
                raise ValueError(f"{key}: use a valid JSON-quoted string: {error.msg}") from None
        elif raw.startswith("'"):
            if not re.fullmatch(r"'(?:[^']|'')*'", raw):
                raise ValueError(f"{key}: invalid YAML single-quoted string")
            value = raw[1:-1].replace("''", "'")
        elif raw in ("true", "false"):
            value = raw == "true"
        elif (not re.match(r"[A-Za-z]", raw) or ": " in raw or " #" in raw
              or raw.endswith(":") or raw.lower() in {"null", "yes", "no", "on", "off", "true", "false"}):
            raise ValueError(f"{key}: quote this value or avoid unsupported YAML syntax")
        else:
            value = raw
        if key not in TEXT_FIELDS | BOOL_FIELDS:
            raise ValueError(f"unsupported metadata field: {key}")
        if key in TEXT_FIELDS and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f"{key} must be a nonempty string")
        if key in BOOL_FIELDS and not isinstance(value, bool):
            raise ValueError(f"{key} must be true or false")
        metadata[key] = value
    for key in ("name", "description"):
        if key not in metadata:
            raise ValueError(f"missing required field: {key}")
    return metadata, "\n".join(lines[end + 1:])


def validate_library(skills_root):
    """Return (names, errors); paths and bundled links must remain self-contained."""
    skills_root = Path(skills_root)
    errors, names = [], []
    if not skills_root.is_dir():
        return [], [f"skill directory not found: {skills_root}"]
    folders = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not folders:
        return [], [f"no skills found: {skills_root}"]
    for folder in folders:
        prefix = folder.name
        if folder.is_symlink():
            errors.append(f"{prefix}: symlinked skill directories are unsupported")
            continue
        skill = folder / "SKILL.md"
        if not skill.is_file():
            errors.append(f"{prefix}: missing SKILL.md")
            continue
        try:
            metadata, body = parse_frontmatter(skill.read_text(encoding="utf-8"))
            name = metadata["name"]
            if not NAME.fullmatch(name) or len(name) > 64:
                errors.append(f"{prefix}: name must be a lowercase slug of at most 64 characters")
            if name != folder.name:
                errors.append(f"{prefix}: name must match its directory")
            if name in names:
                errors.append(f"{prefix}: duplicate skill name {name}")
            names.append(name)
            if len(metadata["description"]) > 1024:
                errors.append(f"{prefix}: description exceeds 1024 characters")
            if not re.search(r"^# .+", body, re.MULTILINE):
                errors.append(f"{prefix}: missing Markdown title and workflow body")
            if len(body.strip()) < 100:
                errors.append(f"{prefix}: workflow body is empty or incomplete")
            if len(skill.read_text(encoding="utf-8").splitlines()) > 500:
                errors.append(f"{prefix}: move supporting detail out of SKILL.md (over 500 lines)")
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f"{prefix}: {error}")
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                errors.append(f"{prefix}: symlinked resource: {path.relative_to(folder)}")
                continue
            if path.suffix != ".md" or not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as error:
                errors.append(f"{prefix}: cannot read {path.name}: {error}")
                continue
            for match in LINK.finditer(text):
                target = match.group(1)
                parsed = urlsplit(target.strip("<>"))
                if parsed.scheme in ("https", "http", "mailto") or not parsed.path:
                    continue
                if parsed.scheme or parsed.netloc:
                    errors.append(f"{prefix}: unsupported resource link: {target}")
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                if not resolved.is_relative_to(folder.resolve()):
                    errors.append(f"{prefix}: resource link escapes its skill: {target}")
                elif not resolved.exists():
                    errors.append(f"{prefix}: missing linked resource: {target}")
    return names, errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Repository or installed project root (default: this repository).")
    args = parser.parse_args(argv)
    names, errors = validate_library(args.root / ".claude" / "skills")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Validated {len(names)} skills: frontmatter, names, workflow bodies, and bundled links.")
    print("Static validation only; no model calls or external integrations were exercised.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
