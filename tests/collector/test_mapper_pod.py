from n1drill.collector.mapper import pod_from_dict
from n1drill.model.toleration import Toleration

DB_POD = {
    "metadata": {"name": "db-pod", "namespace": "n1drill"},
    "spec": {
        "nodeName": "n1-worker-3",
        "containers": [
            {"name": "db", "resources": {"requests": {"cpu": "250m", "memory": "256Mi"}}},
            {"name": "sidecar", "resources": {"requests": {"cpu": "50m"}}},
        ],
        "tolerations": [
            {
                "key": "n1drill.io/dedicated",
                "operator": "Equal",
                "value": "db",
                "effect": "NoSchedule",
            }
        ],
    },
}


def test_pod_from_dict_sums_container_requests() -> None:
    pod = pod_from_dict(DB_POD)
    assert pod.cpu_request_millicores == 300
    assert pod.memory_request_bytes == 256 * 2**20


def test_pod_from_dict_reads_tolerations_and_node() -> None:
    pod = pod_from_dict(DB_POD)
    assert pod.node_name == "n1-worker-3"
    assert pod.tolerations == (
        Toleration(key="n1drill.io/dedicated", operator="Equal", value="db", effect="NoSchedule"),
    )


def test_bare_pod_has_no_owner() -> None:
    assert pod_from_dict(DB_POD).owner_kind is None


def test_pod_without_requests_counts_as_zero() -> None:
    raw = {
        "metadata": {"name": "no-requests-app-x", "ownerReferences": [{"kind": "ReplicaSet"}]},
        "spec": {"containers": [{"name": "app"}]},
    }
    pod = pod_from_dict(raw)
    assert (pod.cpu_request_millicores, pod.memory_request_bytes) == (0, 0)
    assert pod.owner_kind == "ReplicaSet"
