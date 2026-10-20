#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: write-server-config.sh <server-ip>" >&2
  exit 1
fi

SERVER_IP="$1"

sudo mkdir -p /etc/rancher/rke2

cat <<EOF | sudo tee /etc/rancher/rke2/config.yaml >/dev/null
write-kubeconfig-mode: "0644"
tls-san:
  - ${SERVER_IP}
  - n1-server
node-label:
  - "n1drill.io/role=control-plane"
EOF
