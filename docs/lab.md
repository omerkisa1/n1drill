# Lab kaynak planı

Drill için kullanılacak 4 node'luk lab. Node'lar kasıtlı olarak asimetrik: eşit
kaynaklı node'larla drain sırasında "kaynak yetmedi" senaryosu üretilemez,
bu yüzden `n1-worker-1` diğerlerinden büyük tutuluyor.

| Node          | Rol           | vCPU | RAM    | OS                          |
|---------------|---------------|------|--------|-----------------------------|
| n1-server     | control-plane | 2    | 4 GiB  | Ubuntu 24.04 LTS / Rocky 9  |
| n1-worker-1   | worker        | 4    | 8 GiB  | Ubuntu 24.04 LTS / Rocky 9  |
| n1-worker-2   | worker        | 2    | 4 GiB  | Ubuntu 24.04 LTS / Rocky 9  |
| n1-worker-3   | worker        | 2    | 4 GiB  | Ubuntu 24.04 LTS / Rocky 9  |

Minimum kabul edilebilir kurulum `n1-server` + `n1-worker-1` + `n1-worker-2`
üç node'dur, ancak `n1-worker-3` olmadan drain deneyinde pod'ların
gidebileceği yer çok daralır; mümkünse dördü de kurulmalı.

## Kurulum kaydı (0A.040)

`ansible-playbook site.yml` tamamlandıktan sonra bu bölümü doldur:

| Node        | Private IP | node-label                         |
|-------------|------------|-------------------------------------|
| n1-server   |            | `n1drill.io/role=control-plane`      |
| n1-worker-1 |            | `n1drill.io/size=large`              |
| n1-worker-2 |            | `n1drill.io/size=small`              |
| n1-worker-3 |            | `n1drill.io/size=small`              |

Node kapasite tablosu (`ansible-playbook site.yml --tags 0a034` çıktısından):

```
# buraya yapıştır
```

Snapshot kaydı: `tasks/0A040.md`'deki adımlarla alınan snapshot'ın tarihi ve
adı burada tutulur, böylece Faz 0B'de cluster'ı bozduktan sonra hangi
snapshot'a döneceğini unutmazsın.
