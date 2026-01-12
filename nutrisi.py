from beratbadan import BeratBadan

class Nutrisi(BeratBadan):
    def __init__(self, berat_badan, tinggi_badan, jenis_kelamin):
        super().__init__(berat_badan, tinggi_badan, jenis_kelamin)

    def rekomendasi_nutrisi(self):
        _,kategori = self.menghitungbb()
        match kategori:
            case "Kurus":
                return
            case "Normal":
                return
            case "Berat Badan Berlebih":
                return
            case "Obesitas":
                return