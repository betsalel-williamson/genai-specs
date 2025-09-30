#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status

# Define paths relative to the genai-specs submodule root
GENAI_SPECS_ROOT=$(dirname "$0")
MAIN_PROJECT_ROOT=$(dirname "$GENAI_SPECS_ROOT")

# Check if the current directory is a Git repository
if ! git -C "$MAIN_PROJECT_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "ERROR: This script must be run inside a Git repository."
  exit 1
fi

# Check if '.cursor' is listed as a submodule in the main project's .gitmodules
if ! grep -q '\[submodule "\.cursor"\]' "$MAIN_PROJECT_ROOT/.gitmodules"; then
  echo "ERROR: The '.cursor' project is not configured as a Git submodule in the main repository."
  echo "To add it, navigate to the main repository root ($MAIN_PROJECT_ROOT) and run:"
  echo "  git submodule add git@github.com:betsalel-williamson/genai-specs.git .cursor"
  exit 1
fi

echo "The '.cursor' project is correctly identified as a submodule."

# Verify that .cursor submodule exists and is accessible
CURSOR_SUBMODULE="$MAIN_PROJECT_ROOT/.cursor"

if [ ! -d "$CURSOR_SUBMODULE" ]; then
  echo "ERROR: .cursor submodule directory not found at $CURSOR_SUBMODULE"
  echo "Please ensure the submodule is properly initialized:"
  echo "  git submodule update --init --recursive"
  exit 1
fi

echo "Verified .cursor submodule exists and is accessible."

# Verify that the required directories exist in the submodule
if [ ! -d "$CURSOR_SUBMODULE/rules" ]; then
  echo "ERROR: rules directory not found in .cursor submodule"
  exit 1
fi

if [ ! -d "$CURSOR_SUBMODULE/guidelines" ]; then
  echo "ERROR: guidelines directory not found in .cursor submodule"
  exit 1
fi

echo "Verified rules and guidelines directories exist in .cursor submodule."

echo "Cursor initialization script finished."
echo ""
echo "Next steps:"
echo "1. The '.cursor' submodule is properly configured and accessible"
echo "2. Use '@.cursor/rules/filename.mdc' syntax in Cursor chat to include specific rules"
echo "3. Use '@.cursor/guidelines/category/filename.md' syntax to include detailed guidelines"
echo "4. Rules are automatically scoped and can be invoked manually or based on relevance"
echo ""
echo "Example usage in Cursor chat:"
echo "  '@.cursor/rules/standards-user-story.mdc' - for user story standards"
echo "  '@.cursor/rules/guidelines-typescript.mdc' - for TypeScript guidelines"
echo "  '@.cursor/guidelines/typescript/index.md' - for detailed TypeScript guidelines"
echo "  '@.cursor/rules/process-01-core.mdc' - for core engineering principles"
echo ""
echo "Project structure:"
echo "  your-project/"
echo "  └── .cursor/                     # Git submodule (genai-specs)"
echo "      ├── rules/                   # Rules files (.mdc)"
echo "      ├── guidelines/              # Detailed guidelines (.md)"
echo "      └── README.md                # Documentation"