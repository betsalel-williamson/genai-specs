#!/usr/bin/env bash
# Link skills/ into .cursor/skills for Cursor Agent discovery.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/.cursor"
ln -sfn ../skills "$ROOT/.cursor/skills"
echo "Linked $ROOT/.cursor/skills -> ../skills"
