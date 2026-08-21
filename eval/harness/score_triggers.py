#!/usr/bin/env python3
"""Structural validation for trigger eval JSON sets."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TRIGGER_DIR = ROOT / "eval" / "trigger"


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    skill = data.get("skill")
    evals = data.get("evals")
    if not skill:
        errors.append(f"{path.name}: missing skill field")
    if not isinstance(evals, list) or len(evals) < 10:
        errors.append(f"{path.name}: expected >= 10 eval queries")
        return errors

    should = sum(1 for e in evals if e.get("should_trigger"))
    should_not = len(evals) - should
    if should < 4 or should_not < 4:
        errors.append(f"{path.name}: need balanced should/should-not triggers (got {should}/{should_not})")

    for i, item in enumerate(evals):
        if "query" not in item or "should_trigger" not in item:
            errors.append(f"{path.name}[{i}]: requires query and should_trigger")
    return errors


def main() -> int:
    files = sorted(TRIGGER_DIR.glob("*.json"))
    if not files:
        print("No trigger eval files found", file=sys.stderr)
        return 1

    errors: list[str] = []
    summary: list[dict] = []
    for path in files:
        errors.extend(validate_file(path))
        data = json.loads(path.read_text(encoding="utf-8"))
        evals = data["evals"]
        summary.append(
            {
                "file": path.name,
                "skill": data.get("skill"),
                "total": len(evals),
                "should_trigger": sum(1 for e in evals if e.get("should_trigger")),
                "should_not_trigger": sum(1 for e in evals if not e.get("should_trigger")),
            }
        )

    out = ROOT / "docs" / "skills-migration" / "ab-results" / "trigger-summary.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(files)} trigger eval files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
