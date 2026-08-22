resource "openstack_networking_floatingip_v2" "n1_server_floatingip" {
  pool = data.openstack_networking_network_v2.public_network.name
}

resource "openstack_compute_floatingip_associate_v2" "n1_server_floatingip_attach" {
  floating_ip = openstack_networking_floatingip_v2.n1_server_floatingip.address
  instance_id = openstack_compute_instance_v2.n1_server.id
}

resource "openstack_compute_instance_v2" "n1_server" {
  name      = "n1-server"
  flavor_id = var.n1_server_flavor_id
  key_pair  = openstack_compute_keypair_v2.rke2_key.name
  security_groups = [
    openstack_networking_secgroup_v2.bastion.name,
    openstack_networking_secgroup_v2.internal.name,
  ]

  user_data = <<-EOF
    #cloud-config
    hostname: n1-server
    fqdn: n1-server
    manage_etc_hosts: true
  EOF

  block_device {
    uuid                  = var.ubuntu_image_id
    source_type           = "image"
    destination_type      = "volume"
    volume_size           = 20
    boot_index            = 0
    delete_on_termination = true
  }

  network {
    uuid = openstack_networking_network_v2.rke2_network.id
  }

  depends_on = [openstack_networking_router_interface_v2.rke2_router_interface]
}

resource "openstack_compute_instance_v2" "n1_worker" {
  count = 3

  name            = "n1-worker-${count.index + 1}"
  flavor_id       = var.n1_workers_flavor_id
  key_pair        = openstack_compute_keypair_v2.rke2_key.name
  security_groups = [openstack_networking_secgroup_v2.internal.name]

  user_data = <<-EOF
    #cloud-config
    hostname: n1-worker-${count.index + 1}
    fqdn: n1-worker-${count.index + 1}
    manage_etc_hosts: true
  EOF

  block_device {
    uuid                  = var.ubuntu_image_id
    source_type           = "image"
    destination_type      = "volume"
    volume_size           = 20
    boot_index            = 0
    delete_on_termination = true
  }

  network {
    uuid = openstack_networking_network_v2.rke2_network.id
  }

  depends_on = [openstack_networking_router_interface_v2.rke2_router_interface]
}
