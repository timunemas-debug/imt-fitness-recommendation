class UserProfil:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.riwayat = []

    def regist(self):
        return f"Selamat {self.name}!, Anda berhasil membuat akun"

    def login(self):
        return f"Selamat Datang {self.name}!"

    def cek_data(self):
        if not self.name:
            return "Anda belum memiliki akun, silakan membuat akun!"
        else:
            return "Telah membuat akun!"

    def cek_riwayat(self):
        if not self.riwayat:
            return "Belum ada riwayat apapun"
        else:
            for i,history in enumerate(self.riwayat, start=1):
                print(f"{i}, {history}")