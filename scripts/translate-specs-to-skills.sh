#!/usr/bin/env bash
# Translate legacy genai-specs rules/guidelines into skills/ (successor to spec-translation init scripts).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> Migrating rules to skills/"
python3 scripts/migrate-rules-to-skills.py

echo "==> Creating SDLC asset templates"
python3 scripts/create-skill-templates.py

echo "==> Writing rule deprecation stubs"
python3 scripts/deprecate-rules.py

echo "==> Done. Skills live under skills/"
echo "    Docs: docs/skills-migration/"
echo "    Eval: eval/harness/run_arm.sh [A|B|C|D]"
