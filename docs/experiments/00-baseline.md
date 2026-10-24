# Baseline state

Filled in after `kubectl apply -f experiments/` against the real lab
cluster (0B.003, 0B.006, 0B.026).

## Node capacity

(paste from `ansible-playbook site.yml --tags 0a034`, or `docs/lab.md`)

## Pod → node map

Every workload in `experiments/` after `kubectl apply -f experiments/`
(0B.018) and `kubectl get pods -n n1drill-lab -o wide` (0B.003):

| Workload | Kind | Replicas | Expected placement |
|----------|------|----------|---------------------|
| `django-app` | Deployment | 3 | spread, no constraints |
| `crowded-app` | Deployment | 3 | all on `n1-worker-1` (`nodeSelector: size=large`) |
| `jenkins-0` | StatefulSet | 1 | wherever PVC binds first |
| `bare-pod` | Pod | 1 | spread, no controller |
| `node-agent` | DaemonSet | 1/worker | one per worker, all 3 |
| `db-pod` | Pod | 1 | tolerates `n1-worker-3` taint, not required there |
| `no-requests-app` | Deployment | 3 | spread, zero-cost to the scheduler |
| `backup-job` | Job | 1 | spread |
| `pinned-pod` | Pod | 1 | forced onto `n1-worker-2` via `nodeName` |
| `unschedulable-selector` | Pod | 1 | **Pending** (`disktype: ssd` matches nothing) |
| `fragmentation-probe` | Pod | 1 | **Pending** (no single node has 1500m free) |

Fill in actual node names once applied.

## PVC → PV → node affinity

(filled in at 0B.006, once `jenkins`'s PVC is `Bound` — run
`kubectl get pv -o yaml | yq '.items[].spec.nodeAffinity'`)

## PDB status

| PDB | Target | Rule | Expected `ALLOWED DISRUPTIONS` |
|-----|--------|------|----------------------------------|
| `django-app-locked` | `django-app` | `minAvailable: 3` | `0` |
| `crowded-app-healthy` | `crowded-app` | `maxUnavailable: 1` | `>= 1` |

Confirm with `kubectl -n n1drill-lab get pdb`.
