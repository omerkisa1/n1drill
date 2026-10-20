# Ansible migration plan

The lab moved from manual per-node scripts (`scripts/vm-setup/`,
`scripts/rke2-setup/`) to Terraform for provisioning. The remaining OS-level
config and RKE2 install steps move to Ansible instead of SSH-ing into each
node one by one.

## Already covered by Terraform (no Ansible needed)

- `0A.010` — VM creation
- `0A.012` — hostname (via `cloud-config` user_data)
- `0A.014` — SSH key (via `keypair.tf`)
- `0A.019` / `0A.020` — port access, handled at the security group level

## Moving to Ansible

| Role          | Plan steps      | Hosts        |
|---------------|------------------|--------------|
| `base`        | 0A.013, 0A.015–018 | all 4 nodes |
| `rke2_server` | 0A.021–026       | n1-server    |
| `rke2_agent`  | 0A.027–031       | all workers  |

Each task is tagged with its plan step id (e.g. `0a016`), so a single step
can still be run and reviewed in isolation:

```bash
ansible-playbook site.yml --tags 0a016 --check --diff
# or
ansible-playbook site.yml --step
```

## Planned layout

```
ansible/
  ansible.cfg
  inventory/
    hosts.ini          # [server] n1-server, [workers] n1-worker-1/2/3
  roles/
    base/tasks/main.yml
    rke2_server/tasks/main.yml
    rke2_agent/tasks/main.yml
  site.yml
```

## Status

Design only — not implemented yet. The existing scripts under
`scripts/vm-setup/` and `scripts/rke2-setup/` stay as reference for the
exact commands each Ansible task should run.
