from n1drill.model.node import Node, Taint


def test_node_defaults_to_no_labels_or_taints() -> None:
    node = Node(name="n1-worker-1", allocatable_cpu_millicores=2000, allocatable_memory_bytes=2**31)
    assert node.labels == {}
    assert node.taints == ()


def test_node_keeps_taints() -> None:
    taint = Taint(key="n1drill.io/dedicated", value="db", effect="NoSchedule")
    node = Node(
        name="n1-worker-3",
        allocatable_cpu_millicores=2000,
        allocatable_memory_bytes=2**31,
        taints=(taint,),
    )
    assert node.taints == (taint,)
