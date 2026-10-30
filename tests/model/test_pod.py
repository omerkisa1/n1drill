from n1drill.model.pod import Pod


def test_bare_pod_has_no_controller() -> None:
    pod = Pod(namespace="n1drill", name="bare-pod", node_name="n1-worker-2", owner_kind=None)
    assert not pod.has_controller


def test_replicaset_pod_has_controller() -> None:
    pod = Pod(namespace="n1drill", name="django-app-x", node_name=None, owner_kind="ReplicaSet")
    assert pod.has_controller
