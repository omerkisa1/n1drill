# Only attached to n1-server, the single node holding the floating IP.
resource "openstack_networking_secgroup_v2" "bastion" {
  name        = "n1drill-bastion"
  description = "Public-facing access to n1-server"
}

resource "openstack_networking_secgroup_rule_v2" "bastion_ssh" {
  security_group_id = openstack_networking_secgroup_v2.bastion.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 22
  port_range_max    = 22
  remote_ip_prefix  = var.admin_cidr
}

resource "openstack_networking_secgroup_rule_v2" "bastion_kube_api" {
  security_group_id = openstack_networking_secgroup_v2.bastion.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 6443
  port_range_max    = 6443
  remote_ip_prefix  = var.admin_cidr
}

# Attached to all 4 nodes, cluster-internal traffic only (self-referencing).
resource "openstack_networking_secgroup_v2" "internal" {
  name        = "n1drill-internal"
  description = "RKE2 traffic between n1-server and the workers"
}

resource "openstack_networking_secgroup_rule_v2" "internal_ssh" {
  security_group_id = openstack_networking_secgroup_v2.internal.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 22
  port_range_max    = 22
  remote_group_id   = openstack_networking_secgroup_v2.internal.id
}

resource "openstack_networking_secgroup_rule_v2" "internal_rke2_supervisor" {
  security_group_id = openstack_networking_secgroup_v2.internal.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 9345
  port_range_max    = 9345
  remote_group_id   = openstack_networking_secgroup_v2.internal.id
}

resource "openstack_networking_secgroup_rule_v2" "internal_etcd" {
  security_group_id = openstack_networking_secgroup_v2.internal.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 2379
  port_range_max    = 2380
  remote_group_id   = openstack_networking_secgroup_v2.internal.id
}

resource "openstack_networking_secgroup_rule_v2" "internal_kubelet" {
  security_group_id = openstack_networking_secgroup_v2.internal.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "tcp"
  port_range_min    = 10250
  port_range_max    = 10250
  remote_group_id   = openstack_networking_secgroup_v2.internal.id
}

resource "openstack_networking_secgroup_rule_v2" "internal_vxlan" {
  security_group_id = openstack_networking_secgroup_v2.internal.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "udp"
  port_range_min    = 8472
  port_range_max    = 8472
  remote_group_id   = openstack_networking_secgroup_v2.internal.id
}

resource "openstack_networking_secgroup_rule_v2" "internal_icmp" {
  security_group_id = openstack_networking_secgroup_v2.internal.id
  direction         = "ingress"
  ethertype         = "IPv4"
  protocol          = "icmp"
  remote_group_id   = openstack_networking_secgroup_v2.internal.id
}
