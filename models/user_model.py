import hashlib
from config.database import get_connection, get_last_error


class UserModel:
    def __init__(self):
        self.conn = get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Enkripsi satu arah menggunakan SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def _ensure_connection(self):
        """Coba sambung ulang jika koneksi belum ada (misal MySQL baru dinyalakan)."""
        if self.conn is None:
            self.conn = get_connection()
        return self.conn is not None

    def autentikasi(self, username, password):
        # Bedakan "koneksi gagal" dari "username/password salah"
        if not self._ensure_connection():
            raise ConnectionError(
                "Tidak dapat terhubung ke database MySQL.\n"
                f"Detail: {get_last_error()}\n"
                "Pastikan MySQL di Laragon sudah menyala."
            )

        cursor = self.conn.cursor(dictionary=True)
        try:
            password_hash = self.hash_password(password)
            query = (
                f"SELECT id_user, username, role FROM {self.table_name} "
                "WHERE username = %s AND password = %s"
            )
            cursor.execute(query, (username, password_hash))
            return cursor.fetchone()  # None jika kredensial salah
        finally:
            cursor.close()

    def register_user(self, username, password, role='anggota'):
        """Menambahkan user baru dengan password ter-hash SHA-256 (Tugas Poin 1)"""
        if not self._ensure_connection():
            return False, f"Koneksi database gagal: {get_last_error()}"
        try:
            cursor = self.conn.cursor()
            password_hash = self.hash_password(password)

            query = f"INSERT INTO {self.table_name} (username, password, role) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, password_hash, role))

            self.conn.commit()
            cursor.close()
            return True, "Registrasi berhasil!"
        except Exception as err:
            return False, f"Terjadi kesalahan: {err}"