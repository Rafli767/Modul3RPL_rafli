import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.model = BukuModel()
        self.view = BukuView()
        self.user_role = user_role  # Menyimpan role pengguna yang sedang login

        # Mengubah judul window agar menampilkan role yang sedang aktif
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Menyimpan ID buku yang sedang dipilih di tabel
        self.selected_id = None

        # Binding tombol dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Binding event ketika baris tabel diklik
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)

        # --- PENERAPAN OTORISASI (ROLE-BASED ACCESS CONTROL) ---
        if self.user_role == "anggota":
            # Jika role adalah anggota, kunci form input dan nonaktifkan tombol aksi tulis/ubah/hapus
            self.view.btn_simpan.configure(state="disabled", text="Simpan (Admin Only)")
            self.view.btn_update.configure(state="disabled", text="Update (Admin Only)")
            self.view.btn_delete.configure(state="disabled", text="Hapus (Admin Only)")
            
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        # Memuat data ke tabel saat pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        # Validasi Otorisasi: Anggota tidak boleh menambah data
        if self.user_role == "anggota":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.clear_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def pilih_data_tabel(self, event):
        # Mengambil data dari baris tabel yang diklik
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item)
            values = item_data['values']
            
            if values:
                self.selected_id = values[0]
                
                # Jika admin, masukkan data ke form input untuk memudahkan update
                if self.user_role == "admin":
                    self.clear_form()
                    self.view.entry_judul.insert(0, values[1])
                    self.view.entry_penulis.insert(0, values[2])
                    self.view.entry_tahun.insert(0, values[3])

    def update_data(self):
        # Validasi Otorisasi: Anggota tidak boleh mengubah data
        if self.user_role == "anggota":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin diperbarui terlebih dahulu!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(self.selected_id, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.clear_form()
            self.muat_data_tabel()
            self.selected_id = None
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        # Validasi Otorisasi: Anggota tidak boleh menghapus data
        if self.user_role == "anggota":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel yang ingin dihapus terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if konfirmasi:
            if self.model.delete_buku(self.selected_id):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.clear_form()
                self.muat_data_tabel()
                self.selected_id = None
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def clear_form(self):
        # Hanya bersihkan form jika statusnya aktif (untuk admin)
        if self.user_role == "admin":
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')

    def run(self):
        self.view.mainloop()