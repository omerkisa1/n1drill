from n1drill.collector.mapper import node_from_dict
from n1drill.model.node import Taint

WORKER_3 = {
    "metadata": {"name": "n1-worker-3", "labels": {"kubernetes.io/hostname": "n1-worker-3"}},
    "spec": {"taints": [{"key": "n1drill.io/dedicated", "value": "db", "effect": "NoSchedule"}]},
    "status": {"allocatable": {"cpu": "2", "memory": "3880Mi"}},
}


def test_node_from_dict_parses_allocatable() -> None:
    node = node_from_dict(WORKER_3)
    assert node.allocatable_cpu_millicores == 2000
    assert node.allocatable_memory_bytes == 3880 * 2**20


def test_node_from_dict_parses_taints_and_labels() -> None:
    node = node_from_dict(WORKER_3)
    assert node.taints == (Taint(key="n1drill.io/dedicated", value="db", effect="NoSchedule"),)
    assert node.labels == {"kubernetes.io/hostname": "n1-worker-3"}


def test_node_from_dict_without_taints() -> None:
    raw = {"metadata": {"name": "n"}, "status": {"allocatable": {"cpu": "1", "memory": "1Gi"}}}
    assert node_from_dict(raw).taints == ()
