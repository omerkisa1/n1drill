from n1drill.model.node import Node
from n1drill.model.pod import Pod
from n1drill.simulator.fit import fits_resources

NODE = Node(name="n1-worker-1", allocatable_cpu_millicores=2000, allocatable_memory_bytes=4 * 2**30)


def _pod(cpu: int, memory: int) -> Pod:
    return Pod(
        namespace="n1drill",
        name="p",
        node_name=None,
        owner_kind=None,
        cpu_request_millicores=cpu,
        memory_request_bytes=memory,
    )


def test_fits_on_empty_node() -> None:
    assert fits_resources(_pod(1500, 2**30), NODE, used_cpu_millicores=0, used_memory_bytes=0)


def test_exact_fit_is_allowed() -> None:
    assert fits_resources(_pod(500, 2**30), NODE, used_cpu_millicores=1500, used_memory_bytes=0)


def test_cpu_shortage_does_not_fit() -> None:
    assert not fits_resources(_pod(600, 0), NODE, used_cpu_millicores=1500, used_memory_bytes=0)


def test_memory_shortage_does_not_fit() -> None:
    assert not fits_resources(
        _pod(0, 2**30), NODE, used_cpu_millicores=0, used_memory_bytes=4 * 2**30
    )
