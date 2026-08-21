#!/usr/bin/env bash
# Run migration verification matrix: validate skills, trigger sets, and A/B arm logs.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
RESULTS="$ROOT/docs/skills-migration/ab-results"
mkdir -p "$RESULTS"

echo "==> Validating skills/"
python3 scripts/validate-skills.py

echo "==> Validating trigger eval sets"
python3 eval/harness/score_triggers.py

echo "==> Validating SDLC scenario structure"
python3 eval/harness/validate_scenarios.py

echo "==> Generating A/B arm run logs"
for arm in A B C D; do
  bash eval/harness/run_arm.sh "$arm"
done

SUMMARY="$RESULTS/matrix-summary.json"
python3 - <<'PY'
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(".")
results = root / "docs/skills-migration/ab-results"
skills = list((root / "skills").rglob("SKILL.md"))
summary = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "skill_count": len(skills),
    "trigger_summary": json.loads((results / "trigger-summary.json").read_text()),
    "scenario_dirs": sorted(p.name for p in (root / "eval/sdlc").iterdir() if p.is_dir()),
    "arms": sorted(p.name for p in results.glob("arm-*.md")),
    "gate": "Run agent scenarios per eval/sdlc/*; Arm B must beat Arm A on primary behavioral metrics",
}
out = results / "matrix-summary.json"
out.write_text(json.dumps(summary, indent=2) + "\n")
print(f"Wrote {out}")
PY

echo "==> Matrix complete. See $SUMMARY"
