resource "openstack_compute_keypair_v2" "rke2_key" {
  name       = "n1drill-key"
  public_key = file(pathexpand(var.ssh_public_key_path))
}
