from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menentukan data tiruan (mock data) yang dikembalikan oleh database
    mock_cursor.fetchall.return_value = [
        {"id_buku": 1, "judul": "Buku Testing", "penulis": "Penulis QA", "tahun_terbit": 2026}
    ]

    # Melakukan eksekusi fungsi
    hasil = model.get_all_buku()

    # Memverifikasi apakah hasil berupa list dan berisi data
    assert isinstance(hasil, list)
    assert len(hasil) > 0
    assert hasil[0]["judul"] == "Buku Testing"

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()