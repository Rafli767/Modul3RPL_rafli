import hashlib
from config.database import get_connection

class UserModel:
    def __init__(self):
        self.conn = get_connection()
        self.table_name = "users"

    @staticmethod
    def hash_password(password):
        # Enskripsi satu arah menggunakan SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def autentikasi(self, username, password):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            password_hash = self.hash_password(password)
            
            # Parameterized Query untuk mencegah SQL Injection
            query = f"SELECT id_user, username, role FROM {self.table_name} WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password_hash))
            user = cursor.fetchone()
            cursor.close()
            return user
        return None