#!/usr/bin/env bash
set -euo pipefail

sudo systemctl enable --now rke2-server.service
