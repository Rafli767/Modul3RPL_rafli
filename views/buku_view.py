import customtkinter as ctk
from tkinter import ttk, messagebox

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class BukuView(ctk.CTk):
    def __init__(self, role="admin"):
        super().__init__()
        self.role = role  # Menyimpan role user yang sedang aktif
        self.title("Sistem Manajemen Perpustakaan - Koleksi Buku")
        self.geometry("950x580")
        self.resizable(False, False)

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
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
        ).pack(pady=(20, 10))

        self.entry_judul = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Judul Buku", 
            height=38, fg_color="white", text_color="black", border_color="#D1D5DB"
        )
        self.entry_judul.pack(pady=6, padx=20, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Penulis", 
            height=38, fg_color="white", text_color="black", border_color="#D1D5DB"
        )
        self.entry_penulis.pack(pady=6, padx=20, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_kiri, placeholder_text="Masukkan Tahun Terbit", 
            height=38, fg_color="white", text_color="black", border_color="#D1D5DB"
        )
        self.entry_tahun.pack(pady=6, padx=20, fill="x")

        # Tombol Aksi
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri, text="Simpan Data", height=35, 
            fg_color="#16A34A", hover_color="#15803D", font=("Segoe UI", 12, "bold")
        )
        self.btn_simpan.pack(pady=(15, 6), padx=20, fill="x")

        self.btn_update = ctk.CTkButton(
            self.frame_kiri, text="Perbarui Data (Update)", height=35, 
            fg_color="#2563EB", hover_color="#1D4ED8", font=("Segoe UI", 12, "bold")
        )
        self.btn_update.pack(pady=6, padx=20, fill="x")

        self.btn_delete = ctk.CTkButton(
            self.frame_kiri, text="Hapus Data (Delete)", height=35, 
            fg_color="#DC2626", hover_color="#B91C1C", font=("Segoe UI", 12, "bold")
        )
        self.btn_delete.pack(pady=6, padx=20, fill="x")

        # Tombol Logout (Tugas Poin 3) -> Terhubung langsung ke fungsi handle_logout di bawah
        self.btn_logout = ctk.CTkButton(
            self.frame_kiri, text="Logout", height=35, 
            fg_color="#4B5563", hover_color="#374151", font=("Segoe UI", 12, "bold"),
            command=self.handle_logout
        )
        self.btn_logout.pack(pady=(15, 10), padx=20, fill="x")

        # Terapkan Aturan Otorisasi RBAC (Tugas Poin 2)
        self.terapkan_otorisasi()

        # ==================================
        # FRAME KANAN: TABEL DAFTAR BUKU
        # ==================================
        self.frame_kanan = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        self.frame_kanan.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(
            self.frame_kanan, text="Daftar Koleksi Buku", 
            text_color="#1F2937", font=("Segoe UI", 18, "bold")
        ).pack(pady=(20, 2))
        
        ctk.CTkLabel(
            self.frame_kanan, text="Rafli_085", 
            text_color="#61646C", font=("Segoe UI", 12, "bold")
        ).pack(pady=(0, 15))

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="white", foreground="#1F2937", rowheight=30, font=("Segoe UI", 11))
        style.configure("Treeview.Heading", background="#E5E7EB", foreground="#1F2937", font=('Segoe UI', 11, 'bold'))

        kolom = ("Id", "Judul", "Penulis", "Tahun")
        self.tabel = ttk.Treeview(self.frame_kanan, columns=kolom, show="headings", height=12)
        self.tabel.heading("Id", text="ID Buku")
        self.tabel.heading("Judul", text="Judul Buku")
        self.tabel.heading("Penulis", text="Penulis")
        self.tabel.heading("Tahun", text="Tahun Terbit")

        self.tabel.column("Id", width=70, anchor="center")
        self.tabel.column("Judul", width=200, anchor="w")
        self.tabel.column("Penulis", width=160, anchor="w")
        self.tabel.column("Tahun", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(self.frame_kanan, orient="vertical", command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=scrollbar.set)
        
        self.tabel.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=15)
        scrollbar.pack(side="right", fill="y", pady=15, padx=(0, 20))

    def terapkan_otorisasi(self):
        """Mengunci tombol update & delete jika role adalah anggota"""
        if self.role == "anggota":
            self.entry_judul.configure(state="disabled")
            self.entry_penulis.configure(state="disabled")
            self.entry_tahun.configure(state="disabled")
            
            self.btn_simpan.configure(state="disabled", fg_color="#53A470", text="Simpan (Admin Only)")
            self.btn_update.configure(state="disabled", fg_color="#6487C3", text="Update (Admin Only)")
            self.btn_delete.configure(state="disabled", fg_color="#D16161", text="Hapus (Admin Only)")

    def handle_logout(self):
        """Fungsi Logout yang benar dan berada di dalam kelas BukuView"""
        if messagebox.askyesno("Konfirmasi Logout", "Apakah Anda yakin ingin keluar dari sistem?"):
            self.destroy()
            from controllers.auth_controller import AuthController
            auth = AuthController()
            auth.run()