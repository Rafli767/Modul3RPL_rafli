from config.database import get_connection

class BukuModel:
    def __init__(self):
        self.conn = get_connection()

    def get_all_buku(self):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM buku"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def create_buku(self, judul, penulis, tahun):
        try:
            cursor = self.conn.cursor()
            query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
            cursor.execute(query, (judul, penulis, int(tahun)))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saat menyimpan: {e}")
            return False

    def update_buku(self, id_buku, judul, penulis, tahun):
        try:
            cursor = self.conn.cursor()
            query = "UPDATE buku SET judul = %s, penulis = %s, tahun_terbit = %s WHERE id_buku = %s"
            cursor.execute(query, (judul, penulis, int(tahun), id_buku))
            self.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saat update: {e}")
            return False

    def delete_buku(self, id_buku):
        try:
            cursor = self.conn.cursor()
            query = "DELETE FROM buku WHERE id_buku = %s"
            cursor.execute(query, (id_buku,))
            self.conn.commit()
            
            # Cek apakah tabel buku sekarang sudah kosong
            cursor.execute("SELECT COUNT(*) FROM buku")
            jumlah_data = cursor.fetchone()[0]
            
            # Jika tabel kosong, reset AUTO_INCREMENT kembali ke 1
            if jumlah_data == 0:
                cursor.execute("ALTER TABLE buku AUTO_INCREMENT = 1")
                self.conn.commit()
                
            cursor.close()
            return True
        except Exception as e:
            print(f"Error saat hapus: {e}")
            return False