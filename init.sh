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

# Check if 'genai-specs' is listed as a submodule in the main project's .gitmodules
if ! grep -q '\[submodule "genai-specs"\]' "$MAIN_PROJECT_ROOT/.gitmodules"; then
  echo "ERROR: The 'genai-specs' project is not configured as a Git submodule in the main repository."
  echo "To add it, navigate to the main repository root ($MAIN_PROJECT_ROOT) and run:"
  echo "  git submodule add git@github.com:betsalel-williamson/genai-specs.git genai-specs"
  exit 1
fi

echo "The 'genai-specs' project is correctly identified as a submodule."

# Define the .env file path (relative to the main project root)
ENV_FILE="$MAIN_PROJECT_ROOT/.env"

# Define the dummy variables
GOOGLE_CLOUD_PROJECT_VAR='GOOGLE_CLOUD_PROJECT="your-project-id-here"'
GEMINI_MODEL_VAR='GEMINI_MODEL="gemini-2.5-flash"'
GEMINI_API_KEY_VAR='GEMINI_API_KEY="your-api-key-here"'

# Create .env file if it doesn't exist
if [ ! -f "$ENV_FILE" ]; then
  touch "$ENV_FILE"
  echo "Created empty $ENV_FILE"
else
  echo "$ENV_FILE file already exists"
fi

# Function to add or warn about environment variables
add_or_warn_env_var() {
  local var_name="$1"
  local var_value="$2"
  if grep -q "^$var_name=" "$ENV_FILE"; then
    echo "Skipping $var_name because it already exists in $ENV_FILE."
  else
    echo "$var_value" >> "$ENV_FILE"
    echo "Added $var_name to $ENV_FILE."
  fi
}

# Add dummy variables if they don't exist in the .env file
add_or_warn_env_var "GOOGLE_CLOUD_PROJECT" "$GOOGLE_CLOUD_PROJECT_VAR"
add_or_warn_env_var "GEMINI_MODEL" "$GEMINI_MODEL_VAR"
add_or_warn_env_var "GEMINI_API_KEY" "$GEMINI_API_KEY_VAR"

# Define the .gemini/settings.json file path and content (relative to the main project root)
GEMINI_SETTINGS_DIR="$MAIN_PROJECT_ROOT/.gemini"
GEMINI_SETTINGS_FILE="$GEMINI_SETTINGS_DIR/settings.json"
GEMINI_SETTINGS_CONTENT='''{
  "tools": {
    "autoAccept": true,
    "exclude": [
      "EditTool"
    ]
  },
  "context": {
    "fileName": "genai-specs/README.md",
    "fileFiltering": {
      "respectGitIgnore": true,
      "enableRecursiveFileSearch": true
    }
  },
  "mcpServers": {
    "Context7": {
      "command": "npx",
      "args": [
        "-y",
        "@upstash/context7-mcp"
      ]
    }
  }
}'''

# Create .gemini directory if it doesn't exist
if [ ! -d "$GEMINI_SETTINGS_DIR" ]; then
  mkdir -p "$GEMINI_SETTINGS_DIR"
  echo "Created directory $GEMINI_SETTINGS_DIR"
fi

# Handle .gemini/settings.json
if [ -f "$GEMINI_SETTINGS_FILE" ]; then
  CURRENT_SETTINGS=$(cat "$GEMINI_SETTINGS_FILE")
  if [ "$CURRENT_SETTINGS" != "$GEMINI_SETTINGS_CONTENT" ]; then
    echo "$GEMINI_SETTINGS_FILE already exists and its content differs from the default."
    echo "Current content:"
    echo "$CURRENT_SETTINGS"
    echo "Default content:"
    echo "$GEMINI_SETTINGS_CONTENT"
    echo "Please review and update manually if necessary. Skipping overwrite."
  else
    echo "$GEMINI_SETTINGS_FILE already exists and matches the default content. Skipping overwrite."
  fi
else
  echo "$GEMINI_SETTINGS_CONTENT" > "$GEMINI_SETTINGS_FILE"
  echo "Created $GEMINI_SETTINGS_FILE"
fi

# --- Check and add .env to main .gitignore (superproject's .gitignore) ---
MAIN_GITIGNORE="$MAIN_PROJECT_ROOT/.gitignore"

if [ ! -f "$MAIN_GITIGNORE" ]; then
  touch "$MAIN_GITIGNORE"
  echo "Created empty $MAIN_GITIGNORE."
fi

# Check if .env is ignored in the main .gitignore
if ! grep -q ".env" "$MAIN_GITIGNORE"; then
  echo "" >> "$MAIN_GITIGNORE" # Add a newline for separation if file doesn't end with one
  echo ".env" >> "$MAIN_GITIGNORE"
  echo "Added .env to $MAIN_GITIGNORE"
else
  echo ".env is already ignored in $MAIN_GITIGNORE"
fi

echo "Initialization script finished."