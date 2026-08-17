# VM provisioning

4 node, `docs/lab.md`'deki kaynak planına göre oluşturulur: `n1-server`,
`n1-worker-1`, `n1-worker-2`, `n1-worker-3`.

## OS seçimi

Ubuntu 24.04 LTS veya Rocky 9. `scripts/vm-setup/` altındaki scriptler
Ubuntu (apt, netplan, ufw) için yazıldı; Rocky kullanılacaksa paket yöneticisi
(`dnf`), ağ yönetimi (`nmcli`) ve firewall (`firewall-cmd`) karşılıklarını
kendin uygulaman gerekir.

## Nasıl oluşturulur

Hangi hipervizör/sağlayıcı kullanılırsa kullanılsın (VirtualBox, Proxmox,
libvirt/KVM, bulut sağlayıcı, bare metal...), her node için:

1. `docs/lab.md`'deki vCPU/RAM değerlerine göre VM'i oluştur.
2. Ubuntu 24.04 LTS veya Rocky 9 kur, SSH erişimini aç.
3. VM'in en az bir ağ arayüzü olduğundan ve dışarıdan (geliştirme
   makinesinden) erişilebilir olduğundan emin ol.

## Kabul kriteri

Dördü de ayakta ve SSH ile erişilebilir olmalı:

```bash
ssh <user>@<n1-server-ip> hostname
ssh <user>@<n1-worker-1-ip> hostname
ssh <user>@<n1-worker-2-ip> hostname
ssh <user>@<n1-worker-3-ip> hostname
```

Minimum kabul edilebilir kurulum server + 2 worker'dır, ancak
`n1-worker-3` olmadan drain deneyinde pod'ların gidebileceği yer daralır.

Devamı için: `scripts/vm-setup/` altındaki scriptler, `0A.011`'den başlayarak
her adımda sırayla çalıştırılır.
