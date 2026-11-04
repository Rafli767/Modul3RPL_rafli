import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController


class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView()
        self.view.btn_login.configure(command=self.proses_login)

    def proses_login(self):
        # .strip() agar spasi yang tidak sengaja terketik diabaikan
        username = self.view.entry_username.get().strip()
        password = self.view.entry_password.get().strip()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
            return

        # Bedakan: koneksi gagal / error database / kredensial salah
        try:
            user = self.model.autentikasi(username, password)
        except ConnectionError as e:
            messagebox.showerror("Koneksi Gagal", str(e))
            return
        except Exception as e:
            messagebox.showerror(
                "Kesalahan Database",
                f"{type(e).__name__}: {e}"
            )
            return

        if not user:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")
            return

        # autentikasi() memakai cursor(dictionary=True), jadi hasilnya dict
        user_name = user.get("username", "User")
        user_role = user.get("role", "petugas")

        messagebox.showinfo("Login Berhasil", f"Selamat datang, {user_name} ({user_role})!")
        self.view.destroy()

        # Membuka halaman utama sesuai role
        app_utama = BukuController(role=user_role)
        app_utama.run()

    def run(self):
        self.view.mainloop()