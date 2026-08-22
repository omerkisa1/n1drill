variable "portvmind_username" { type = string }
variable "portvmind_password" { type = string }
variable "portvmind_application_credential_id" { type = string }
variable "portvmind_application_credential_secret" { type = string }
variable "tenant_id" { type = string }
variable "ubuntu_image_id" { type = string }
variable "n1_server_flavor_id" { type = string }
variable "n1_workers_flavor_id" { type = string }
variable "external_network_id" { type = string }

variable "admin_cidr" {
  type        = string
  description = "Your IP (as a /32) allowed to reach n1-server over SSH and the kube-apiserver"
}

variable "ssh_public_key_path" {
  type    = string
  default = "~/.ssh/id_ed25519.pub"
}

variable "private_subnet_cidr" {
  type    = string
  default = "10.20.0.0/24"
}

