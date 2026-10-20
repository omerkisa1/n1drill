#!/usr/bin/env bash
set -euo pipefail

LINE1='export KUBECONFIG=/etc/rancher/rke2/rke2.yaml'
LINE2='export PATH=$PATH:/var/lib/rancher/rke2/bin'

for LINE in "$LINE1" "$LINE2"; do
  if ! grep -qxF "$LINE" "$HOME/.bashrc" 2>/dev/null; then
    echo "$LINE" >> "$HOME/.bashrc"
  fi
done
