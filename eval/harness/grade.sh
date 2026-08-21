#!/usr/bin/env bash
# Grade eval run outputs against eval_metadata.json assertions.
set -euo pipefail

RUN_DIR="${1:?Usage: grade.sh <run-directory>}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
GRADER="$ROOT/skills/_meta/skill-creator/agents/grader.md"

if [[ ! -d "$RUN_DIR" ]]; then
  echo "Run directory not found: $RUN_DIR" >&2
  exit 1
fi

echo "Grading $RUN_DIR"
echo "Use grader instructions: $GRADER"
echo "Write grading.json per run with fields: text, passed, evidence"

find "$RUN_DIR" -name 'eval_metadata.json' -print
