#!/usr/bin/env bash
# Run A/B/C/D evaluation arms for SDLC skills migration.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
ARM="${1:-B}"
OUT="$ROOT/docs/skills-migration/ab-results/arm-${ARM}-$(date +%Y%m%d-%H%M%S).md"

mkdir -p "$(dirname "$OUT")"

case "$ARM" in
  A)
    CONFIG="Legacy .mdc rules (manual @ inclusion)"
    SKILLS="rules/"
    ;;
  B)
    CONFIG="Full skills/ library"
    SKILLS="skills/"
    ;;
  C)
    CONFIG="skills/ + MCP listSkills/getSkill"
    SKILLS="skills/ + .mcp/skills-server.json"
    ;;
  D)
    CONFIG="SDLC + engineering skills only (no domains/)"
    SKILLS="skills/{_meta,sdlc,engineering,verification}/"
    ;;
  *)
    echo "Usage: $0 [A|B|C|D]" >&2
    exit 1
    ;;
esac

cat >"$OUT" <<EOF
# A/B Arm ${ARM} Run

- **Configuration:** ${CONFIG}
- **Context root:** ${SKILLS}
- **Date:** $(date -u +"%Y-%m-%dT%H:%M:%SZ")

## Scenarios

Run each scenario in \`eval/sdlc/\` with clean-room prompts (no hints about rules under test).

## Metrics

Record primary behavioral metrics from agent-verification-protocol:

- TDD order compliance
- Tidy First separation
- User story non-technical AC rate
- Type-safety violations
- Premature task completion claims

## Trigger evals

Use JSON sets in \`eval/trigger/\` for precision/recall when Arm involves skills.

## Aggregation

After manual or agent runs, grade with:

\`\`\`bash
eval/harness/grade.sh <run-directory>
eval/harness/aggregate.sh <run-directory>
\`\`\`

Gate: Arm B must beat Arm A on primary metrics with stable trigger rates (>=3 reps).
EOF

echo "Wrote $OUT"
echo "Arm: $ARM — $CONFIG"
