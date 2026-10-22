# Baseline state

Filled in after `kubectl apply -f experiments/` against the real lab
cluster (0B.003, 0B.006, 0B.026).

## Node capacity

(paste from `ansible-playbook site.yml --tags 0a034`, or `docs/lab.md`)

## Pod → node map

| Pod | Node | Notes |
|-----|------|-------|
| django-app-xxx | | |
| django-app-yyy | | |
| django-app-zzz | | |

## PVC → PV → node affinity

(filled in at 0B.006, once `jenkins` StatefulSet exists)

## PDB status

(filled in at 0B.009/0B.010)
