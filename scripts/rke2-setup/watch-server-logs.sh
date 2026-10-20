#!/usr/bin/env bash
set -euo pipefail

sudo journalctl -u rke2-server -f
