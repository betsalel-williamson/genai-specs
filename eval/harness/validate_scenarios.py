#!/usr/bin/env python3
"""Validate SDLC behavioral scenario eval directories."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCENARIO_ROOT = ROOT / "eval" / "sdlc"


def main() -> int:
    errors: list[str] = []
    dirs = [p for p in SCENARIO_ROOT.iterdir() if p.is_dir()]
    if not dirs:
        print("No scenario directories found", file=sys.stderr)
        return 1

    for directory in sorted(dirs):
        scenarios = directory / "scenarios.json"
        if not scenarios.exists():
            errors.append(f"{directory.name}: missing scenarios.json")
            continue
        data = json.loads(scenarios.read_text(encoding="utf-8"))
        items = data.get("scenarios", [])
        if len(items) < 1:
            errors.append(f"{directory.name}: no scenarios defined")
        for item in items:
            if not item.get("prompt") or not item.get("assertions"):
                errors.append(f"{directory.name}: scenario missing prompt or assertions")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"Validated {len(dirs)} scenario directories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
