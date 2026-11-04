# Sistem Informasi Perpustakaan (MVC & DevOps Module)

Aplikasi desktop berbasis Python (*CustomTkinter*) dan basis data MySQL yang menerapkan prinsip keamanan *Role-Based Access Control* (RBAC), *SHA-256 Hashing*, dan *Parameterized Queries*.

## 1. Deskripsi Singkat Aplikasi

Sistem Informasi Perpustakaan ini dirancang dengan arsitektur **MVC (Model-View-Controller)** untuk memudahkan pengelolaan data buku, anggota, dan transaksi peminjaman. Aplikasi ini dilengkapi dengan sistem keamanan modern untuk melindungi data kredensial pengguna serta mendukung pengemasan mandiri (*standalone executable*).

## 2. Struktur Direktori (MVC)

```
modul3/
├── .github/workflows/
│   └── ci_pipeline.yml      # Konfigurasi CI (GitHub Actions)
├── config/
│   └── database.py          # Konfigurasi koneksi MySQL
├── models/                  # Logika basis data dan kueri SQL
├── views/                   # Antarmuka grafis (CustomTkinter)
├── controllers/             # Alur logika bisnis dan hak akses (RBAC)
├── tests/                   # Pengujian otomatis (pytest)
├── main.py                  # Titik masuk aplikasi
├── requirements.txt         # Daftar dependensi
└── README.md
```

- `models/`: Berisi skrip yang mengelola logika basis data dan kueri SQL.
- `views/`: Berisi skrip antarmuka grafis pengguna (*Graphical User Interface*) menggunakan pustaka *CustomTkinter*.
- `controllers/`: Mengatur alur logika bisnis aplikasi serta hak akses berbasis peran (*RBAC*: Admin vs Anggota).
- `tests/`: Berisi skrip pengujian otomatis menggunakan *pytest*.

## 3. Panduan Instalasi & Konfigurasi Database MySQL

### 3.1 Prasyarat

- **Python 3.10+**
- **MySQL Server** (disarankan memakai [Laragon](https://laragon.org/))
- **Git**

### 3.2 Instalasi

1. Kloning repositori:
   ```bash
   git clone https://github.com/HQID/modul3.git
   cd modul3
   ```
2. Buat dan aktifkan *virtual environment*:
   ```bash
   python -m venv env
   env\Scripts\activate    # Untuk Windows
   ```
3. Instal seluruh dependensi:
   ```bash
   pip install -r requirements.txt
   ```

### 3.3 Konfigurasi Database MySQL

1. Nyalakan MySQL (di Laragon klik **Start All**).
2. Buka phpMyAdmin atau HeidiSQL, lalu jalankan skrip berikut:
   ```sql
   CREATE DATABASE IF NOT EXISTS perpustakaan;
   USE perpustakaan;

   CREATE TABLE IF NOT EXISTS users (
       id_user  INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       password VARCHAR(64) NOT NULL,        -- hash SHA-256
       role     VARCHAR(20) NOT NULL DEFAULT 'anggota'
   );

   CREATE TABLE IF NOT EXISTS buku (
       id_buku      INT AUTO_INCREMENT PRIMARY KEY,
       judul        VARCHAR(150) NOT NULL,
       penulis      VARCHAR(100) NOT NULL,
       tahun_terbit INT NOT NULL
   );

   -- Akun admin awal (password: admin123)
   INSERT INTO users (username, password, role)
   VALUES ('admin', SHA2('admin123', 256), 'admin');
   ```
3. Sesuaikan koneksi di `config/database.py` dengan MySQL Anda:
   ```python
   host="127.0.0.1",
   port=3306,
   user="root",
   password="",
   database="perpustakaan",
   ```

## 4. Cara Menjalankan Aplikasi

### Dari kode sumber

Pastikan MySQL sudah menyala dan *virtual environment* aktif, lalu jalankan:

```bash
python main.py
```

Login menggunakan akun yang terdaftar di tabel `users` (contoh: `admin` / `admin123`).

### Dari berkas `.exe`

1. Unduh `AplikasiPerpustakaan.exe` dari halaman [Releases](https://github.com/HQID/modul3/releases).
2. Pastikan MySQL sudah menyala.
3. Klik dua kali `AplikasiPerpustakaan.exe`.

### Membangun berkas `.exe` sendiri

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name "AplikasiPerpustakaan" --collect-all mysql.connector --collect-all customtkinter main.py
```

Hasilnya tersimpan di folder `dist/`.

## 5. Menjalankan Pengujian

```bash
python -m pytest -v
```

Pengecekan kualitas kode (linter):

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
```

Kedua perintah ini juga dijalankan otomatis oleh GitHub Actions pada setiap *push* dan *pull request* ke branch `main`.