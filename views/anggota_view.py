import customtkinter as ctk
from tkinter import ttk

# Mengatur tema terang
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Anggota")
        self.geometry("850x520")
        self.resizable(False, False)

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)  # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=2)  # Kolom Kanan (Tabel)
        self.grid_rowconfigure(0, weight=1)

        # ==================================
        # FRAME KIRI: FORMULIR INPUT ANGGOTA
        # ==================================
        self.frame_kiri = ctk.CTkFrame(self, fg_color="#E0E0E0", corner_radius=0)
        self.frame_kiri.grid(row=0, column=0, sticky="nsew")

        ctk.CTkLabel(self.frame_kiri, text="Form Data Anggota", text_color="black", font=("Arial", 16, "bold")).pack(pady=15)

        # Komponen Input Form
        self.entry_nama = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Nama Anggota", fg_color="white", text_color="black", border_color="#B0B0B0")
        self.entry_nama.pack(pady=10, padx=15, fill="x")

        self.entry_alamat = ctk.CTkEntry(self.frame_kiri, placeholder_text="Masukkan Alamat Anggota", fg_color="white", text_color="black", border_color="#B0B0B0")
        self.entry_alamat.pack(pady=10, padx=15, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", fg_color="green")
        self.btn_simpan.pack(pady=(20, 5), padx=15, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", fg_color="blue")
        self.btn_update.pack(pady=5, padx=15, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", fg_color="red")
        self.btn_delete.pack(pady=5, padx=15, fill="x")

        # ==================================
        # FRAME KANAN: TABEL DAFTAR ANGGOTA
        # ==================================
        self.frame_kanan = ctk.CTkFrame(self, fg_color="#D9D9D9", corner_radius=0)
        self.frame_kanan.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(self.frame_kanan, text="Daftar Anggota Perpustakaan", text_color="black", font=("Arial", 16, "bold")).pack(pady=(15, 5))
        ctk.CTkLabel(self.frame_kanan, text="Rafli_085", text_color="black", font=("Arial", 12, "bold")).pack(pady=(0, 10))

        # Styling untuk ttk.Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
        style.configure("Treeview.Heading", background="white", foreground="black", font=('Arial', 10, 'bold'))

        # Komponen Tabel (Treeview) dengan kolom: ID, Nama Anggota, Alamat
        kolom = ("Id", "Nama", "Alamat")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=13)

        # Konfigurasi Header Tabel
        self.tabel.heading("Id", text="ID Anggota")
        self.tabel.heading("Nama", text="Nama Anggota")
        self.tabel.heading("Alamat", text="Alamat")

        # Konfigurasi Lebar Kolom
        self.tabel.column("Id", width=90, anchor="center")
        self.tabel.column("Nama", width=180, anchor="w")
        self.tabel.column("Alamat", width=230, anchor="w")

        self.tabel.pack(fill="both", expand=True, padx=15, pady=10)


# Blok eksekusi untuk menguji tampilan grafis
if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()