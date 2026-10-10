from config.database import get_connection

from config.database import get_connection

class BukuModel:
    def __init__(self):
        self.db = get_connection() 
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
            val = (judul, penulis, tahun_terbit)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False
#sambungan untuk tugas 4 RPL

class BukuModel:
    def __init__(self):
        self.db = get_connection()

    def create_buku(self, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
        val = (judul, penulis, tahun_terbit)
        cursor.execute(query, val)
        self.db.commit()
        cursor.close()

    def get_all_buku(self):
        cursor = self.db.cursor(dictionary=True)
        query = "SELECT * FROM buku"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    # --- TAMBAHKAN DUA METODE DI BAWAH INI ---
    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        cursor = self.db.cursor()
        query = "UPDATE buku SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
        val = (judul, penulis, tahun_terbit, id_buku)
        cursor.execute(query, val)
        self.db.commit()
        cursor.close()

    def delete_buku(self, id_buku):
        cursor = self.db.cursor()
        query = "DELETE FROM buku WHERE id_buku = %s"
        val = (id_buku,)
        cursor.execute(query, val)
        self.db.commit()
        cursor.close()