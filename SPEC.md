# SPEC

## Finding taxonomy

The simulator's output is a list of findings, each tagged with one of the
codes below. The code is a classification of *why* a pod can't run where
it's expected to, derived directly from what we actually observed in the
lab (`docs/experiments/`). Code comes from this table — not the other way
around.

| Finding code | Finding | Why | Which scenario | Severity | Evidence |
|---|---|---|---|---|---|
| `INSUFFICIENT_RESOURCES` | Pod stays `Pending` — no single node has enough free CPU/memory for it | Scheduler needs one node that satisfies the full request; partial fits across multiple nodes don't count | `fragmentation-probe` | High | `experiments/11-fragmentation-probe.yaml`, `docs/experiments/00-baseline.md` |
| `UNTOLERATED_TAINT` | Pod can't land on an otherwise-fitting node because it doesn't tolerate that node's taint | `n1-worker-3` carries `n1drill.io/dedicated=db:NoSchedule`; only pods with a matching toleration can schedule there | `db-pod` vs. `n1-worker-3` | Medium | `experiments/09-tolerating-pod.yaml`, `ansible/roles/lab_experiments/tasks/main.yml` (0b012 taint) |
| `SELECTOR_MISMATCH` | Pod stuck `Pending` because its `nodeSelector` matches zero nodes | `unschedulable-selector` asks for `disktype=ssd`, no lab node carries that label | `unschedulable-selector` | High | `experiments/08-unschedulable-selector.yaml`, `docs/experiments/00-baseline.md` |
| `NOT_RESCHEDULABLE` | Workload has no owning controller, so it isn't recreated when its node is lost | `bare-pod` and `pinned-pod` are plain Pods with no ReplicaSet/Job/StatefulSet above them | drain and crash of `n1-worker-2` | Critical | `experiments/04-bare-pod.yaml`, `experiments/13-pinned-pod.yaml`, `docs/experiments/01-drain-prediction.md`, `docs/experiments/06-crash-prediction.md` |
| `VOLUME_BOUND` | Pod can't move to another node because its PV is already pinned there | `local-path` PVs get a `nodeAffinity` for whichever node first claimed them (`WaitForFirstConsumer`); `jenkins-0` can't follow itself off that node | `jenkins-0` during drain/crash | High | `experiments/03-jenkins-statefulset.yaml`, `docs/experiments/01-drain-prediction.md` |
| `REPLICA_CONCENTRATION` | Multiple replicas of one workload land on the same node, so a single node loss removes more capacity than expected | No anti-affinity rules are set anywhere in the lab; the scheduler is free to co-locate `django-app`/`no-requests-app` replicas | drain or crash of whichever node holds the concentration | Medium | `experiments/01-django-app.yaml`, `docs/experiments/01-drain-prediction.md` (expected pod count section) |
| `PDB_BLOCKED` | Voluntary eviction is refused because it would violate a PodDisruptionBudget | `django-app`'s PDB sets `minAvailable: 3` against 3 replicas — zero disruptions allowed before the drain even starts | `kubectl drain n1-worker-2` | High | `experiments/06-pdb-locked.yaml`, `docs/experiments/01-drain-prediction.md` |
| `FRAGMENTATION` | Cluster-wide free capacity looks sufficient in aggregate, but it's spread thin across nodes so nothing fits it in one place | Same symptom class as `INSUFFICIENT_RESOURCES` but called out separately: the failure is about distribution, not total supply | `fragmentation-probe` | High | `experiments/11-fragmentation-probe.yaml`, `docs/experiments/00-baseline.md` (capacity table) |
| `MISSING_REQUESTS` | Pod has no `resources.requests`, so the scheduler treats it as free and it can crowd out capacity-aware workloads | `no-requests-app` defines no requests block at all | general crowding risk, not a single scenario | Low | `experiments/10-no-requests.yaml` |
| `PERMANENT_LOSS` | A workload disappears with no automatic path back — nothing will ever recreate it | `bare-pod`/`pinned-pod` during an **involuntary** disruption (the node crashes instead of being drained) | crash of `n1-worker-2` | Critical | `docs/experiments/06-crash-prediction.md` |
| `UNKNOWN` | Catch-all for a scheduling failure that doesn't match any pattern above | Reserved so the tool reports "I don't know why" instead of guessing or silently dropping the pod | none — no manifest in this lab is designed to trigger it | — | `docs/experiments/00-baseline.md` (negative evidence: if this code ever fires against the lab fixtures, that's a classifier bug, not a real finding) |

## Output format

_To be filled in at 0B.044, once real `kubectl describe` scheduler
messages have been captured from the live drain run — this section needs
actual wording, not a guess._
