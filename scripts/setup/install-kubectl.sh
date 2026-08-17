#!/usr/bin/env bash
set -euo pipefail

STAGING_DIR="$HOME/.cache/n1drill"
mkdir -p "$STAGING_DIR"
cd "$STAGING_DIR"

KUBECTL_VERSION="$(curl -Ls https://dl.k8s.io/release/stable.txt)"
curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256) kubectl" | sha256sum --check

if [ "$(id -u)" = "0" ]; then
  install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
else
  mkdir -p "$HOME/.local/bin"
  install -m 0755 kubectl "$HOME/.local/bin/kubectl"
fi
