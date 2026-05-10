# 🛡️ Cybersecurity Portfolio – Diky Ari Setiyawan

**Junior Penetration Tester | Security Enthusiast | Continuous Learner**

Selamat datang di portofolio saya! Repositori ini adalah kumpulan dokumentasi perjalanan saya mendalami keamanan siber dari membangun lab pribadi hingga menyelesaikan tantangan Capture The Flag, menulis alat sendiri, dan menganalisis malware.  


[![GitHub last commit|116](https://img.shields.io/github/last-commit/DikyArs/cybersecurity-portfolio?color=blue&style=flat-square)](https://github.com/DikyArs/cybersecurity-portfolio)
[![Repo Size|112](https://img.shields.io/github/repo-size/DikyArs/cybersecurity-portfolio?style=flat-square)](https://github.com/DikyArs/cybersecurity-portfolio)

---

## 🗂️ Daftar Isi
- [🔬 Lab Pribadi](#-lab-pribadi)
- [⚔️ Skenario Serangan](#️-skenario-serangan)
- [🧪 TryHackMe Write-ups](#-tryhackme-write-ups)
- [🐍 Proyek & Skrip](#-proyek--skrip)
- [📊 Analisis Malware](#-analisis-malware)
- [📓 Jurnal Pembelajaran](#-jurnal-pembelajaran)
- [🛠️ Tools & Teknologi](#️-tools--teknologi)
-  [📫 Kontak](#-kontak)

---

## 🔬 Lab Pribadi
Saya membangun lingkungan aman menggunakan **VirtualBox** untuk praktik langsung.
- **Penyerang:** Debian Linux dengan alat-alat penetration testing.
- **Target:** Metasploitable 2, mesin yang sengaja rentan.
- **Jaringan:** Host-only (isolasi penuh).

📄 **[Dokumentasi Setup Lab](HomeLab/Setup-Guide.md)**  
🔗 Diagram, spesifikasi perangkat, langkah instalasi.

---

## ⚔️ Skenario Serangan
### Eksploitasi vsftpd 2.3.4 Backdoor (Tanpa Metasploit)
Memanfaatkan backdoor pada layanan FTP untuk mendapatkan akses root hanya dengan `nc`.
- **Target:** Metasploitable 2
- **CVE:** CVE-2011-2523
- **Hasil:** Remote root shell dalam hitungan detik.

📄 **[Write-up Lengkap](HomeLab/Attack-Scenarios/vsftpd-backdoor.md)**

---

## 🧪 TryHackMe Write-ups
### RootMe
Web enumeration, bypass upload filter, reverse shell, dan SUID privilege escalation.
- **Skills:** Gobuster, Netcat, Python privileges.

📄 **[Write-up RootMe](TryHackMe-Rooms/RootMe.md)**

---

## 🐍 Proyek & Skrip
### Port Scanner TCP (Python)
Skrip pemindaian port sederhana yang saya tulis dari nol untuk memahami socket programming.
- **Fitur:** Input interaktif, timeout koneksi, penanganan error.

📂 **[Lihat Proyek](Scripts-Tools/port-scanner/)**

---

## 📊 Analisis Malware
### Analisis Statis Varian Mirai
Menggunakan `strings`, `file`, dan VirusTotal untuk mengidentifikasi IOC tanpa mengeksekusi sampel.
- **Sumber:** MalwareBazaar
- **Label:** Trojan.Linux.Mirai

📄 **[Laporan Analisis](Projects/Malware-Analysis-1/Report.md)**

---

## 📓 Jurnal Pembelajaran
Catatan reflektif dari hari ke hari, tantangan yang dihadapi, dan skill yang dipelajari.

📖 **[Baca Jurnal](Learning-Journal.md)**

---

## 🛠️ Tools & Teknologi
- **Sistem Operasi:** Debian, Ubuntu Server (Metasploitable)
- **Security Tools:** Nmap, Burp Suite (dasar), Netcat, Metasploit, Wireshark
- **Scripting:** Python, Bash
- **Platform:** TryHackMe, Hack The Box (coming soon)
- **Analisis:** VirusTotal, Binwalk, Strings
- **Virtualisasi:** VirtualBox

---

## 📫 Kontak
- **LinkedIn:** [linkedin.com/in/diky-ari-s](https://linkedin.com/in/diky-ari-s)
- **Email:** [dikyarisetiyawan@gmail.com](mailto:dikyarisetiyawan@gmail.com)

**Saya sangat antusias untuk belajar dan berkontribusi di tim keamanan.** 


