#!/usr/bin/env bash
# Aggregate graded runs into benchmark summary.
set -euo pipefail

RUN_DIR="${1:?Usage: aggregate.sh <run-directory>}"
SKILL_NAME="${2:-sdlc-migration}"

OUT="$RUN_DIR/benchmark.json"
MD="$RUN_DIR/benchmark.md"

python3 - <<PY
import json
from pathlib import Path

run = Path("$RUN_DIR")
grading_files = list(run.rglob("grading.json"))
results = []
for gf in grading_files:
    data = json.loads(gf.read_text())
    expectations = data.get("expectations", [])
    passed = sum(1 for e in expectations if e.get("passed"))
    total = len(expectations) or 1
    results.append({
        "run": str(gf.parent.relative_to(run)),
        "pass_rate": round(passed / total, 3),
        "passed": passed,
        "total": total,
    })

summary = {
    "skill_name": "$SKILL_NAME",
    "runs": results,
    "mean_pass_rate": round(sum(r["pass_rate"] for r in results) / max(len(results), 1), 3),
}
Path("$OUT").write_text(json.dumps(summary, indent=2) + "\n")
lines = ["# Benchmark Summary", "", f"Skill: $SKILL_NAME", f"Mean pass rate: {summary['mean_pass_rate']}", ""]
for r in results:
    lines.append(f"- {r['run']}: {r['pass_rate']} ({r['passed']}/{r['total']})")
Path("$MD").write_text("\n".join(lines) + "\n")
print("Wrote", "$OUT", "and", "$MD")
PY
