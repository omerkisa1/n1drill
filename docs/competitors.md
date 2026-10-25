# Competitor analysis

One question per tool: does it simulate a node-loss scenario (drain or
crash) before it happens, or does it only show what the cluster looks
like right now?

| Tool | Does it simulate node loss, or just show current state? |
|---|---|
| `kube-capacity` | Just current state — it's a `kubectl top`-style view of allocatable vs. requested per node, no what-if removal. |
| `kubectl-view-allocations` | Just current state — same category as `kube-capacity`, a nicer allocation table, nothing predictive. |
| `robusta/krr` | Just current state (historically) — recommends `requests`/`limits` from past Prometheus usage, has no concept of a node disappearing. |
| `goldilocks` | Just current state (historically) — runs VPA in recommendation mode per workload, same resource-right-sizing angle as `krr`, no node-loss modeling. |
| `descheduler` | Neither, really — it's a live rebalancer that evicts pods against policies on a real cluster; it reacts after the fact instead of predicting what a loss would do. |
| `cluster-autoscaler`'s simulator package | Closest match, but internal-only — CA's scale-down path simulates "could every pod on this node be rescheduled elsewhere" before removing a node, which is exactly n1drill's question, but it's a private library used by CA itself, not a tool you point at a cluster to ask the question yourself. |
| `kube-scheduler-simulator` | Partial — it's a web UI that replays the real scheduler's decision process step by step, useful for watching *why* a given pod landed where it did, but you drive it by hand (add/remove pods and nodes yourself); it doesn't produce a drain/crash report on its own. |

None of them answer "if I lose this specific node right now, what breaks
and why" as a single command. That gap is the project.
