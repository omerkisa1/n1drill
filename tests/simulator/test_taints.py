from n1drill.model.node import Node, Taint
from n1drill.model.pod import Pod
from n1drill.model.toleration import Toleration
from n1drill.simulator.taints import blocking_taints

DB_TAINT = Taint(key="n1drill.io/dedicated", value="db", effect="NoSchedule")
WORKER_3 = Node(
    name="n1-worker-3",
    allocatable_cpu_millicores=2000,
    allocatable_memory_bytes=2**31,
    taints=(DB_TAINT,),
)


def _pod(*tolerations: Toleration) -> Pod:
    return Pod(
        namespace="n1drill", name="p", node_name=None, owner_kind=None, tolerations=tolerations
    )


def test_untolerated_taint_blocks() -> None:
    assert blocking_taints(_pod(), WORKER_3) == [DB_TAINT]


def test_tolerated_taint_does_not_block() -> None:
    db_pod = _pod(Toleration(key="n1drill.io/dedicated", value="db", effect="NoSchedule"))
    assert blocking_taints(db_pod, WORKER_3) == []


def test_prefer_no_schedule_never_blocks() -> None:
    soft = Taint(key="k", value="v", effect="PreferNoSchedule")
    node = Node(
        name="n", allocatable_cpu_millicores=1000, allocatable_memory_bytes=2**30, taints=(soft,)
    )
    assert blocking_taints(_pod(), node) == []
