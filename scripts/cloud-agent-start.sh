#!/usr/bin/env bash
# Readiness check for the genai-specs docs linting toolchain.
# This repository has no long-running service; "starting" simply verifies that
# the linting tools are available so an agent can immediately lint docs.
set -euo pipefail

fail=0

if command -v vale >/dev/null 2>&1; then
  echo "vale: $(vale -v)"
else
  echo "ERROR: vale is not installed. Run scripts/cloud-agent-setup.sh." >&2
  fail=1
fi

if [ -x node_modules/.bin/markdownlint-cli2 ]; then
  echo "markdownlint-cli2: present"
else
  echo "ERROR: markdownlint-cli2 is not installed. Run scripts/cloud-agent-setup.sh (npm install)." >&2
  fail=1
fi

if [ "$fail" -ne 0 ]; then
  exit 1
fi

echo "Docs linting toolchain ready."
echo "  Markdown lint : npm run format"
echo "  Prose lint    : vale --config .vale.ini --minAlertLevel error ."
