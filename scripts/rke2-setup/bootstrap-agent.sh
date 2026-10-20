#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "usage: bootstrap-agent.sh <server-ip> <node-token> <node-label>" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

sudo "$SCRIPT_DIR/install-agent.sh"
sudo "$SCRIPT_DIR/write-agent-config.sh" "$1" "$2" "$3"
"$SCRIPT_DIR/start-agent.sh"
