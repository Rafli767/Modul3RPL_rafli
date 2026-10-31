import hashlib
from config.database import get_connection

class UserModel:
    def __init__(self):
        self.conn = get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Enkripsi satu arah menggunakan SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)
            
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None

    def register_user(self, username, password, role='anggota'):
        """Menambahkan user baru dengan password ter-hash SHA-256 (Tugas Poin 1)"""
        if self.conn:
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
        return False, "Koneksi database gagal."