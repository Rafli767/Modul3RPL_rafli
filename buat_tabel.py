from config.database import get_connection

def buat_tabel_buku():
    db = get_connection()
    cursor = db.cursor()
    
    # Perintah SQL untuk membuat tabel buku
    query = """
    CREATE TABLE IF NOT EXISTS buku (
        id_buku INT AUTO_INCREMENT PRIMARY KEY,
        judul VARCHAR(255) NOT NULL,
        penulis VARCHAR(255) NOT NULL,
        tahun_terbit INT NOT NULL
    )
    """
    
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()
    print("Tabel 'buku' berhasil dibuat!")

if __name__ == "__main__":
    buat_tabel_buku()