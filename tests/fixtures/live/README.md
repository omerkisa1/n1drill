# Live fixtures

Real `kubectl get ... -o yaml` dumps from the n1drill lab cluster
(`ansible-playbook site.yml --tags 0b020,0b021,0b022,0b023`), cleaned with
`scripts/experiments/clean-fixtures.sh`. Faz 2's mapper tests run against
these.

## Decision: internal IPs are not masked

These fixtures keep real private IPs (`10.20.0.0/24`, matching
`terraform/variables.tf`'s `private_subnet_cidr`). That range already
appears in `ansible/inventory/hosts.ini.example` and `docs/lab.md`, isn't
routable from outside the lab network, and carries no identifying
information beyond "this is a private subnet somewhere" - masking it would
just make the fixtures harder to cross-reference with the rest of the repo
for no real privacy gain.

What `clean-fixtures.sh` does still strip: `metadata.managedFields` (pure
noise) and anything secret-shaped (tokens, certificates, passwords) - those
get checked for and the script fails loudly if any show up.
