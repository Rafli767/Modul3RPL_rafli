import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.selected_id = None

        # Mengikat butang dengan fungsi
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_data_tabel)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.clear_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def pilih_data_tabel(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item)
            values = item_data['values']
            if values:
                self.selected_id = values[0]
                self.clear_form()
                self.view.entry_nama.insert(0, values[1])
                self.view.entry_alamat.insert(0, values[2])

    def clear_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def run(self):
        self.view.mainloop()