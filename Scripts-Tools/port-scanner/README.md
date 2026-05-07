# Port Scanner TCP Sederhana

**Bahasa:** Python 3  
**Fungsi:** Memindai port TCP 1–1024 pada target yang diberikan.  
**Digunakan untuk:** Latihan enumerasi dasar di lab pribadi.

---
## Cara Menjalankan

```
python3 port_scanner.py
```

Kemudian masukkan alamat IP target.

![[port-scanner-output.png]]

---
## Fitur

- Input IP target.
    
- Timeout koneksi singkat hanya 1 detik agar proses cepat.
    
- Hanya menampilkan port terbuka.
    
- Penanganan error (jika host tidak ditemukan, maka koneksi gagal).

---

## Batasan

- Hanya TCP, lambat untuk rentang besar.

