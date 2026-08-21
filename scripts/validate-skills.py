#!/usr/bin/env python3
"""Validate genai-specs Agent Skills (agentskills.io + Cursor extensions)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

ALLOWED_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
    "paths",
    "disable-model-invocation",
}

NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    if not text.startswith("---"):
        return {}, "missing frontmatter"
    end = text.find("\n---", 3)
    if end == -1:
        return {}, "unclosed frontmatter"
    block = text[3:end].strip()
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            return {}, f"invalid frontmatter line: {line!r}"
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, None


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: SKILL.md not found"]

    text = skill_md.read_text(encoding="utf-8")
    fm, err = parse_frontmatter(text)
    if err:
        return [f"{skill_dir}: {err}"]

    extra = set(fm) - ALLOWED_KEYS
    if extra:
        errors.append(f"{skill_dir}: unexpected frontmatter keys: {', '.join(sorted(extra))}")

    name = fm.get("name", "")
    folder = skill_dir.name
    if name != folder:
        errors.append(f"{skill_dir}: name '{name}' must match folder '{folder}'")

    if not NAME_RE.match(name):
        errors.append(f"{skill_dir}: invalid name '{name}'")

    desc = fm.get("description", "")
    if "_meta/skill-creator" not in str(skill_dir).replace("\\", "/"):
        if not desc.startswith("Use when"):
            errors.append(f"{skill_dir}: description must start with 'Use when'")
    if len(desc) > 1024:
        errors.append(f"{skill_dir}: description exceeds 1024 chars")

    body = text.split("---", 2)[2] if text.count("---") >= 2 else ""
    if len(body.splitlines()) > 520:
        errors.append(f"{skill_dir}: SKILL.md body exceeds ~500 lines; shard to references/")

    return errors


def find_skill_dirs() -> list[Path]:
    dirs: list[Path] = []
    for skill_md in SKILLS_ROOT.rglob("SKILL.md"):
        dirs.append(skill_md.parent)
    return sorted(dirs)


def main() -> int:
    all_errors: list[str] = []
    skill_dirs = find_skill_dirs()
    if not skill_dirs:
        print("No skills found under skills/", file=sys.stderr)
        return 1

    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    print(f"Validated {len(skill_dirs)} skills")
    if all_errors:
        for err in all_errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print("All skills valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
