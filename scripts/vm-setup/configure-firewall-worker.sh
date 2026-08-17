#!/usr/bin/env bash
set -euo pipefail

# Ports needed on RKE2 worker (agent) nodes.
# 10250/tcp - kubelet
# 8472/udp  - VXLAN (Canal/Flannel)

sudo ufw allow 10250/tcp
sudo ufw allow 8472/udp

sudo ufw status
