import os
import sys
import datetime
import mysql.connector

_last_error = ""


def _log_path():
    # Simpan log di samping file .exe (atau di folder proyek saat dijalankan lewat VS Code)
    base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.getcwd()
    return os.path.join(base, "error_log.txt")


def get_last_error():
    return _last_error


def get_connection():
    global _last_error
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",        # lebih aman daripada "localhost" (hindari masalah IPv6)
            port=3306,               # cek port MySQL di Laragon jika berbeda
            user="root",
            password="",
            database="perpustakaan",
            connection_timeout=5,
            use_pure=True,           # pakai implementasi Python murni, lebih stabil di PyInstaller
        )
        _last_error = ""
        return connection
    except Exception as err:         # Exception, bukan hanya mysql.connector.Error
        _last_error = str(err)
        try:
            with open(_log_path(), "a", encoding="utf-8") as f:
                f.write(f"[{datetime.datetime.now()}] {type(err).__name__}: {err}\n")
        except Exception:
            pass
        return None