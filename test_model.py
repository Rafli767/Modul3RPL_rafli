from models.anggota_model import AnggotaModel

anggota_model = AnggotaModel()

# 1. Menguji Create Data Anggota
print("=== Tambah Anggota ===")
anggota_model.create_anggota("Andi Saputra", "Jl. Tamalanrea Raya")
anggota_model.create_anggota("Nurul Hidayah", "Jl. AP Pettarani")
print("Data berhasil ditambahkan!")

# 2. Menguji Read Data Anggota (Sebelum Update/Delete jika ada)
print("\n=== Daftar Anggota ===")
daftar_anggota = anggota_model.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")