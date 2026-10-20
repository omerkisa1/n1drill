#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "usage: write-agent-config.sh <server-ip> <node-token> <node-label>" >&2
  echo "  example node-label: n1drill.io/size=large" >&2
  exit 1
fi

SERVER_IP="$1"
TOKEN="$2"
NODE_LABEL="$3"

sudo mkdir -p /etc/rancher/rke2

cat <<EOF | sudo tee /etc/rancher/rke2/config.yaml >/dev/null
server: https://${SERVER_IP}:9345
token: ${TOKEN}
node-label:
  - "${NODE_LABEL}"
EOF

sudo chmod 600 /etc/rancher/rke2/config.yaml
