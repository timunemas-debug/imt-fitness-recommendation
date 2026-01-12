class BeratBadan:
    def __init__(self, berat_badan, tinggi_badan, jenis_kelamin):
        self.berat_badan = berat_badan
        self.tinggi_badan = tinggi_badan
        self.jenis_kelamin = jenis_kelamin

    def menghitungbb(self):
        tinggi_bd = self.tinggi_badan / 100
        imt = self.berat_badan / (tinggi_bd ** 2)
         
        if imt < 18.5:
            kategori = "Kurus"
        elif 18.5 <= imt < 25:
            kategori = "Normal"
        elif 25 <= imt < 30:
            kategori = "Berat Badan Berlebih"
        else:
            kategori = "Obesitas"
        return round(imt, 2), kategori
    
    def rekomendasi_makanan(self):
        _, kategori = self.menghitungbb()
        match kategori:
            case "Obesitas":
                rekomendasi = """Rekomendasi Makanan Sehat untuk Diet:
                      1. Dada ayam : Bagian dada ayam rendah lemak jenuh dan tinggi protein, cocok dipanggang atau direbus untuk menu diet sehat.
                      2. Telur : Telur kaya protein dan vitamin, bagian putihnya bisa dijadikan sumber energi rendah kalori.
                      3. Daging sapi tanpa lemak : Daging sapi tanpa lemak mengandung zat gizi penting dan sebaiknya diolah dengan cara direbus, dikukus,
                         atau dipanggang.
                      4. Kentang : Kentang rebus atau kukus kaya kalium dan vitamin yang membantu menjaga tekanan darah tetap stabil.
                      5. Kacang-kacangan : Kacang seperti kedelai, kacang merah, dan kacang tanah tinggi serat dan protein, sehingga membuat kenyang lebih lama."""
            case "Kurus":
                rekomendasi = """Cara Menaikan Berat Badan Secara Sehat:
                      1. Tingkatkan porsi makan Makan lebih sering (5 - 6 kali sehari) dengan porsi terkontrol, bukan sekaligus besar.
                      2. Perhatikan pilihan makanan Pilih makanan bergizi seimbang: karbohidrat kompleks (nasi merah, roti gandum),
                         protein tanpa lemak (ikan, ayam tanpa kulit), sayur, buah, kacang, dan produk susu.
                      3. Ngemil sehat Tambahkan camilan bergizi di sela waktu makan, seperti yogurt dengan buah/kacang, smoothies, atau potongan buah.
                      4. Atur kebiasaan minum Hindari minum terlalu banyak sebelum atau saat makan agar tidak cepat kenyang.
                      5. Olahraga rutin Fokus pada latihan angkat beban untuk menambah massa otot, bukan hanya lemak.
                      6. Tidur cukup Terapkan sleep hygiene agar hormon bekerja optimal di malam hari."""
            case "Berat Badan Berlebih":
                rekomendasi = """Rekomendasi Mengontrol Berat Badan:
                      1. Kurangi makanan tinggi gula dan lemak Batasi gorengan, makanan cepat saji, minuman manis, dan makanan olahan.
                      2. Perbanyak serat Konsumsi sayur, buah, dan biji-bijian agar kenyang lebih lama.
                      3. Kontrol porsi makan Makan dengan porsi lebih kecil namun tetap bergizi.
                      4. Aktif bergerak Kombinasikan olahraga kardio (lari, skipping) dan latihan kekuatan.
                      5. Hindari makan larut malam Beri jeda minimal 2 - 3 jam sebelum tidur setelah makan."""
            case "Normal":
                rekomendasi = """Rekomendasi Menjaga Berat Badan Ideal:
                      1. Pola makan seimbang Konsumsi karbohidrat, protein, lemak sehat, sayur, dan buah dengan porsi seimbang.
                      2. Atur jadwal makan Jangan melewatkan sarapan dan usahakan makan teratur 3 kali sehari.
                      3. Perbanyak air putih Minum minimal 8 gelas air per hari untuk membantu metabolisme tubuh.
                      4. Olahraga rutin Lakukan aktivitas fisik minimal 30 menit per hari seperti jalan kaki, jogging, atau bersepeda.
                      5. Istirahat cukup Tidur 7 - 9 jam per hari agar metabolisme tubuh tetap optimal."""
        return rekomendasi