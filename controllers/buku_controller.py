import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Menyimpan ID buku yang sedang dipilih di tabel
        self.selected_id = None

        # Binding tombol dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Binding event ketika baris tabel diklik
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)

        # Memuat data ke tabel saat pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
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
                # Masukkan data ke form input di sebelah kiri
                self.clear_form()
                self.view.entry_judul.insert(0, values[1])
                self.view.entry_penulis.insert(0, values[2])
                self.view.entry_tahun.insert(0, values[3])

    def update_data(self):
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
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def run(self):
        self.view.mainloop()