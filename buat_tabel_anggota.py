from config.database import get_connection

db = get_connection()
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS anggota (
    id_anggota INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(255) NOT NULL,
    alamat TEXT NOT NULL
)
""")
db.commit()
cursor.close()
db.close()
print("Tabel 'anggota' berhasil dibuat!")