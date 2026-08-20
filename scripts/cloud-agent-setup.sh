#!/usr/bin/env bash
# Idempotent setup for the genai-specs docs linting toolchain.
# Installs the `vale` prose-linter binary (a standalone Go binary that is NOT an
# npm package) and then installs Node dependencies. Safe to run repeatedly.
set -euo pipefail

VALE_VERSION="3.18.0"

install_vale() {
  local tmp arch asset
  tmp="$(mktemp -d)"
  arch="$(uname -m)"
  case "$arch" in
    x86_64 | amd64) asset="64-bit" ;;
    aarch64 | arm64) asset="arm64" ;;
    *)
      echo "ERROR: unsupported architecture for vale: $arch" >&2
      exit 1
      ;;
  esac

  echo "Installing vale ${VALE_VERSION} (${arch})..."
  curl -fsSL --retry 3 --retry-delay 2 -o "$tmp/vale.tar.gz" \
    "https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_${asset}.tar.gz"
  tar -xzf "$tmp/vale.tar.gz" -C "$tmp" vale

  if [ -w /usr/local/bin ]; then
    mv "$tmp/vale" /usr/local/bin/vale
    chmod +x /usr/local/bin/vale
  else
    sudo mv "$tmp/vale" /usr/local/bin/vale
    sudo chmod +x /usr/local/bin/vale
  fi
  rm -rf "$tmp"
}

current_vale_version() {
  command -v vale >/dev/null 2>&1 || return 1
  vale -v 2>/dev/null | awk '{print $3}'
}

if [ "$(current_vale_version || true)" != "$VALE_VERSION" ]; then
  install_vale
else
  echo "vale ${VALE_VERSION} already installed."
fi

vale -v

# Installs husky + markdownlint-cli2 and runs the `prepare` script
# (`husky && vale sync`), which downloads the Google vale style package.
echo "Installing Node dependencies..."
npm install

echo "Setup complete."
