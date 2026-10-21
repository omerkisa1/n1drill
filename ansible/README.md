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

| Role            | Covers       | Hosts   |
|-----------------|--------------|---------|
| `base`          | 0A.013, 0A.015-018 | all 4 nodes |
| `rke2_server`   | 0A.021-026 | n1-server |
| `rke2_agent`    | 0A.027-031 | all workers |
| `cluster_verify`| 0A.032-034 | n1-server |
