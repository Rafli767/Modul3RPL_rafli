import customtkinter as ctk
from tkinter import ttk

# Mengatur tema terang
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Manajemen Perpustakaan - Koleksi Buku")
        self.geometry("950x540")
        self.resizable(False, False)

        # Konfigurasi Grid Utama (1 Baris, 2 Kolom)
        self.grid_columnconfigure(0, weight=1)  # Kolom Kiri (Form)
        self.grid_columnconfigure(1, weight=2)  # Kolom Kanan (Tabel)
        self.grid_rowconfigure(0, weight=1)

        # ==================================
        # FRAME KIRI: FORMULIR INPUT BUKU
        # ==================================
        self.frame_kiri = ctk.CTkFrame(self, fg_color="#F4F4F5", corner_radius=0)
        self.frame_kiri.grid(row=0, column=0, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kiri, 
            text="Form Data Buku", 
            text_color="#1F2937", 
            font=("Segoe UI", 16, "bold")
        ).pack(pady=(25, 15))

        # Komponen Input Form dengan tinggi & padding yang lebih nyaman dilihat
        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri, 
            placeholder_text="Masukkan Judul Buku", 
            height=40,
            fg_color="white", 
            text_color="black", 
            border_color="#D1D5DB",
            font=("Segoe UI", 12)
        )
        self.entry_judul.pack(pady=8, padx=20, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri, 
            placeholder_text="Masukkan Penulis", 
            height=40,
            fg_color="white", 
            text_color="black", 
            border_color="#D1D5DB",
            font=("Segoe UI", 12)
        )
        self.entry_penulis.pack(pady=8, padx=20, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri, 
            placeholder_text="Masukkan Tahun Terbit", 
            height=40,
            fg_color="white", 
            text_color="black", 
            border_color="#D1D5DB",
            font=("Segoe UI", 12)
        )
        self.entry_tahun.pack(pady=8, padx=20, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(self.frame_kiri, text="Simpan Data", height=38, fg_color="#16A34A", hover_color="#15803D", font=("Segoe UI", 12, "bold"))
        self.btn_simpan.pack(pady=(25, 8), padx=20, fill="x")

        self.btn_update = ctk.CTkButton(self.frame_kiri, text="Perbarui Data (Update)", height=38, fg_color="#2563EB", hover_color="#1D4ED8", font=("Segoe UI", 12, "bold"))
        self.btn_update.pack(pady=8, padx=20, fill="x")

        self.btn_delete = ctk.CTkButton(self.frame_kiri, text="Hapus Data (Delete)", height=38, fg_color="#DC2626", hover_color="#B91C1C", font=("Segoe UI", 12, "bold"))
        self.btn_delete.pack(pady=8, padx=20, fill="x")

        # ==================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ==================================
        self.frame_kanan = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.frame_kanan.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kanan, 
            text="Daftar Koleksi Buku", 
            text_color="#1F2937", 
            font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 2))
        
        ctk.CTkLabel(
            self.frame_kanan, 
            text="Rafli_085", 
            text_color="#6B7280", 
            font=("Segoe UI", 12, "bold")
        ).pack(pady=(0, 15))

        # Styling untuk ttk.Treeview agar elegan
        style = ttk.Style()
        style.theme_use("default")
        
        # Konfigurasi warna, tinggi baris, dan font tabel
        style.configure(
            "Treeview", 
            background="white", 
            foreground="#1F2937", 
            rowheight=30, 
            fieldbackground="white",
            font=("Segoe UI", 11)
        )
        style.configure(
            "Treeview.Heading", 
            background="#E5E7EB", 
            foreground="#1F2937", 
            font=('Segoe UI', 11, 'bold')
        )
        style.map("Treeview", background=[('selected', '#3B82F6')], foreground=[('selected', 'white')])

        # Komponen Tabel (Treeview)
        kolom = ("Id", "Judul", "Penulis", "Tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=12)

        # Konfigurasi Header Tabel
        self.tabel.heading("Id", text="ID Buku")
        self.tabel.heading("Judul", text="Judul Buku")
        self.tabel.heading("Penulis", text="Penulis")
        self.tabel.heading("Tahun", text="Tahun Terbit")

        # Konfigurasi Lebar & Penjajaran Kolom
        self.tabel.column("Id", width=70, anchor="center")
        self.tabel.column("Judul", width=200, anchor="w")
        self.tabel.column("Penulis", width=160, anchor="w")
        self.tabel.column("Tahun", width=90, anchor="center")

        # Penambahan Scrollbar untuk Tabel agar lebih rapi jika data banyak
        scrollbar = ttk.Scrollbar(self.frame_kanan, orient="vertical", command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=scrollbar.set)
        
        self.tabel.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=15)
        scrollbar.pack(side="right", fill="y", pady=15, padx=(0, 20))

# Blok eksekusi untuk menguji tampilan grafis
if __name__ == "__main__":
    app = BukuView()
    app.mainloop()