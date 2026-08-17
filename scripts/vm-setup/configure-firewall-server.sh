#!/usr/bin/env bash
set -euo pipefail

# Ports needed on the RKE2 server (control-plane) node.
# 6443/tcp   - kube-apiserver
# 9345/tcp   - RKE2 supervisor
# 2379-2380  - etcd client/peer
# 10250/tcp  - kubelet
# 8472/udp   - VXLAN (Canal/Flannel)
# 4240/tcp   - Cilium health check (not needed with the default Canal CNI)

sudo ufw allow 6443/tcp
sudo ufw allow 9345/tcp
sudo ufw allow 2379:2380/tcp
sudo ufw allow 10250/tcp
sudo ufw allow 8472/udp
sudo ufw allow 4240/tcp

sudo ufw status
