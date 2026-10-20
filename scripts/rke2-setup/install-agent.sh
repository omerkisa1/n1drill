#!/usr/bin/env bash
set -euo pipefail

curl -sfL https://get.rke2.io | sudo INSTALL_RKE2_TYPE="agent" sh -
