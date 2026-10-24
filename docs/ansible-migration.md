# Ansible migration plan

The lab moved from manual per-node scripts (`scripts/vm-setup/`,
`scripts/rke2-setup/`) to Terraform for provisioning. The remaining OS-level
config and RKE2 install steps moved to Ansible instead of SSH-ing into each
node one by one.

## Already covered by Terraform (no Ansible needed)

- `0A.010` — VM creation
- `0A.012` — hostname (via `cloud-config` user_data)
- `0A.014` — SSH key (via `keypair.tf`)
- `0A.019` / `0A.020` — port access, handled at the security group level

## Covered by Ansible

| Role               | Plan steps              | Hosts        |
|--------------------|---------------------------|--------------|
| `base`             | 0A.013, 0A.015–018        | all 4 nodes  |
| `rke2_server`      | 0A.021–026                | n1-server    |
| `rke2_agent`       | 0A.027–031                | all workers  |
| `cluster_verify`   | 0A.032–034, 0A.039        | n1-server    |
| `local_kubeconfig` | 0A.035–038                | n1-server (dev-machine actions) |
| `lab_experiments`  | 0B.012, 0B.018–024        | n1-server (dev-machine actions) |

`lab_experiments` is Faz 0B's contribution: applying `experiments/*.yaml`
and dumping the result into `tests/fixtures/live/` for Faz 2's mapper
tests, instead of running each `kubectl` command by hand.

Each task is tagged with its plan step id (e.g. `0a016`), so a single step
can still be run and reviewed in isolation — see `ansible/README.md` for
exact commands (`--tags`, `--step`).

## Status

Implemented. `scripts/vm-setup/` and `scripts/rke2-setup/` stay in the repo
as the reference these roles were written from, but the playbook under
`ansible/` is now the way 0A.013–0A.034 actually get applied.
