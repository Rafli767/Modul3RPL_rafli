# Sistem Informasi Perpustakaan (MVC & DevOps Module)

Aplikasi desktop berbasis Python (*CustomTkinter*) dan basis data MySQL yang menerapkan prinsip keamanan *Role-Based Access Control* (RBAC), *SHA-256 Hashing*, dan *Parameterized Queries*.

## 1. Deskripsi Singkat Aplikasi
Sistem Informasi Perpustakaan ini dirancang dengan arsitektur **MVC (Model-View-Controller)** untuk memudahkan pengelolaan data buku, anggota, dan transaksi peminjaman. Aplikasi ini dilengkapi dengan sistem keamanan modern untuk melindungi data kredensial pengguna serta mendukung pengemasan mandiri (*standalone executable*).

## 2. Struktur Direktori (MVC)
- `models/`: Berisi skrip yang mengelola logika basis data dan kueri SQL.
- `views/`: Berisi skrip antarmuka grafis pengguna (*Graphical User Interface*) menggunakan pustaka *CustomTkinter*.
- `controllers/`: Mengatur alur logika bisnis aplikasi serta hak akses berbasis peran (*RBAC*: Admin vs Anggota).
- `tests/`: Berisi skrip pengujian otomatis menggunakan *pytest*.

## 3. Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan Anda telah menginstal **Python (versinya minimal 3.10+)** dan **MySQL Server**.
2. Buat basis data baru di MySQL sesuai konfigurasi koneksi proyek Anda.
3. Kloning repositori ini ke komputer lokal Anda.
4. Buat dan aktifkan *virtual environment*:
   ```bash
   python -m venv env
   env\Scripts\activate  # Untuk Windows