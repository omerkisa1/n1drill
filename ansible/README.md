# n1drill ansible

Runs the OS-level setup and RKE2 install that used to be done node-by-node
with the scripts in `scripts/vm-setup/` and `scripts/rke2-setup/`.

## Setup

```bash
cp inventory/hosts.ini.example inventory/hosts.ini
# edit hosts.ini with the real IPs from `terraform output`
```

## Run everything

```bash
ansible-playbook site.yml
```

## Run or review one step at a time

```bash
ansible-playbook site.yml --tags 0a016 --check --diff
ansible-playbook site.yml --step
```

## Roles

| Role              | Covers       | Hosts   |
|-------------------|--------------|---------|
| `base`            | 0A.013, 0A.015-018 | all 4 nodes |
| `rke2_server`     | 0A.021-026 | n1-server |
| `rke2_agent`      | 0A.027-031 | all workers |
| `cluster_verify`  | 0A.032-034, 0A.039 | n1-server |
| `local_kubeconfig`| 0A.035-038 | n1-server (actions run on the dev machine via `delegate_to: localhost`) |
| `lab_experiments` | 0B.012, 0B.018-024 | n1-server (actions run on the dev machine) |

`lab_experiments` applies the manifests in `experiments/` and dumps the
resulting state into `tests/fixtures/live/` - run it again any time those
manifests change.
