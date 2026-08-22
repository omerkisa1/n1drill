data "openstack_networking_network_v2" "public_network" {
  network_id = var.external_network_id
}

resource "openstack_networking_network_v2" "rke2_network" {
  name           = "n1drill-network"
  admin_state_up = true
}

resource "openstack_networking_subnet_v2" "rke2_subnet" {
  name            = "n1drill-subnet"
  network_id      = openstack_networking_network_v2.rke2_network.id
  cidr            = var.private_subnet_cidr
  ip_version      = 4
  dns_nameservers = ["1.1.1.1", "8.8.8.8"]
}

resource "openstack_networking_router_v2" "rke2_router" {
  name                = "n1drill-router"
  external_network_id = var.external_network_id
}

resource "openstack_networking_router_interface_v2" "rke2_router_interface" {
  router_id = openstack_networking_router_v2.rke2_router.id
  subnet_id = openstack_networking_subnet_v2.rke2_subnet.id
}
