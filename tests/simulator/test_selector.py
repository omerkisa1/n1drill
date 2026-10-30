from n1drill.model.node import Node
from n1drill.model.pod import Pod
from n1drill.simulator.selector import matches_node_selector

NODE = Node(
    name="n1-worker-1",
    allocatable_cpu_millicores=2000,
    allocatable_memory_bytes=2**31,
    labels={"kubernetes.io/hostname": "n1-worker-1"},
)


def _pod(selector: dict[str, str]) -> Pod:
    return Pod(
        namespace="n1drill", name="p", node_name=None, owner_kind=None, node_selector=selector
    )


def test_empty_selector_matches_any_node() -> None:
    assert matches_node_selector(_pod({}), NODE)


def test_missing_label_does_not_match() -> None:
    assert not matches_node_selector(_pod({"disktype": "ssd"}), NODE)


def test_matching_label_matches() -> None:
    assert matches_node_selector(_pod({"kubernetes.io/hostname": "n1-worker-1"}), NODE)
