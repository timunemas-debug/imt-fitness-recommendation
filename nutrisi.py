from beratbadan import BeratBadan

class Nutrisi(BeratBadan):
    def __init__(self, berat_badan, tinggi_badan, jenis_kelamin):
        super().__init__(berat_badan, tinggi_badan, jenis_kelamin)

    def rekomendasi_nutrisi(self):
        _,kategori = self.menghitungbb()
        match kategori:
            case "Kurus":
                return{
                    "Prinsip Nutrisi: ": "Asupan kalori lebih tinggi dari kebutuhan harian\n"
                                        "Fokus pada protein cukup, karbohidrat kompleks, dan lemak sehat\n"
                                        "Makan 3 kali utama + 2-3 kali selingan",
                    "Rekomendasi Nutrisi: ": "Protein: Daging tanpa lemak, ayam, ikan, telur, susu, yoghurt, tempe, tahu\n"
                                             "Karbohidrat Kompleks: Nasi, Nasi merah, kentang, ubi, oatmeal, roti gandum \n"
                                             "Lemak Sehat: Alpukat, Kacang-kacangan, Biji-bijian, Minyak zaitun\n"
                                             "Sayur dan Buah: Tetap wajib untuk vitamin dan mineral\n"
                                             "Minuman: Susu, Smoothie buah + Protein",
                    "Anjuran Dokter: ": "- Hindari junk food berlebihan kalau ingin gemuk\n"
                                        "- Lakukan latihan kekuatan (resistance training) untuk menambah massa otot"
                }
            case "Normal":
                return{
                     "Prinsip Nutrisi: ": "Asupan kalori seimbang\n"
                                          "Pola makan beragam dan seimbang.",
                    "Rekomendasi Nutrisi: ": "Protein: Ikan, ayam, telur, tempe, tahu, kacang-kacangan\n"
                                             "Karbohidrat: Nasi, gandum, kentang, ubi (secukupnya)\n"
                                             "Lemak Sehat: Ikan berlemak, alpukat, minyak zaitun\n"
                                             "Sayur dan Buah: Minimal 5 porsi per hari\n"
                                             "Air Putih: 2-3 Liter Perhari",
                    "Anjuran Dokter: ": "- Batasi gula, garam, dan makanan ultra-proses\n"
                                        "- Aktivitas fisik rutin minimal 150 menit per minggu"
                }
            case "Berat Badan Berlebih":
                return{
                    "Prinsip Nutrisi: ": "Defisit Kalori ringan-sedang\n"
                                          "Tinggi serat dan protein agar kenyang lebih lama.",
                    "Rekomendasi Nutrisi: ": "Protein: Dada ayam, ikan, telur rebus, tempe, tahu\n"
                                             "Karbohidrat Kompleks: Nasi merah, kentang rebus, oatmeal\n"
                                             "Lemak: Dalam jumlah kecil(Minyak zaitun, Kacang)\n"
                                             "Sayur dan Buah: Diperbanyak (Sayur: Brokoli, Bayam, Wortel, Kol. Buah: Apel, Pir, Pepaya(Hindari Belebihan))",
                    "Yang Harus Dihindari: ": "Gorengan, Minuman Manis, Makanan cepat saji",
                    "Anjuran Dokter: ": "- Penurunan Berat Badan ideal: 0,5-1Kg per minggu\n"
                                        "- Kombinasi diet + olahraga adalah yang terbaik"
                }
            case "Obesitas":
                return{
                    "Prinsip Nutrisi: ": "Defisit kalori terkontrol\n"
                                          "Nutrisi padat gizi, rendah energi.",
                    "Rekomendasi Nutrisi: ": "Protein Tanpa Lemak: Ikan, ayam tanpa kulit, putih telur, tahu, tempe\n"
                                             "Karbohidrat Sangat Dibatasi: Nasi merah, kentang rebus (porsi kecil)\n"
                                             "Lemak: Dalam jumlah kecil(Minyak zaitun, Kacang)\n"
                                             "Sayur Tinggi serat dan Buah: (Sayur: Brokoli, bayam, kol, buncis, timun. Buah: 1-2 porsi per hari\n"
                                             "Air Putih: Sangat dianjurkan, hindari minuman manis",
                    "Yang Harus Dihindari: ": "Minuman manis dan soda, Makanan tinggi gula & lemak jenuh, Makan malam berlebihan",
                    "Anjuran Dokter: ": "- Dianjurkan pengawasan tenaga medis bila obesitas berat\n"
                                        "- Fokus perubahan gaya hidup jangka panjang"
                }
            
    def bulking(self):
        _,kategori = self.menghitungbb()
        match kategori:
            case "Kurus":
                return{
                    "Kebutuhan Kalori: ": "Surplus Kalori: -> +300 sampai +500 kkal per hari dari kebutuhan normal(dokter tidak menyarankan lebih dari ini)",
                    "Takaran Makro Nutrisi(Per-hari): ": "Protein: 1,6-2,2 Gram per Kg berat badan, Contoh: Berat 60Kg, 96-132 gram protein/hari\n"
                                                         "Sumber & Takaran setara: -Dada ayam matang 100 g = ±31 g protein, -Telur utuh 1 butir = ±6 g protein, -Tempe 100 g = ±19 g protein, -Ikan 100 g = ±20-25 g protein\n"
                                                         "Karbohidrat: 4-6 gram per kg berat badan, Contoh: Berat 60Kg, 240-360 gram karbohidrat/hari\n"
                                                         "Sertara Makanan: -Nasi putih matang 100 g ≈ 28 g karbohidrat, -Kentang rebus 100 g ≈ 20 g karbohidrat, -Oatmeal kering 100 g ≈ 66 g karbohidrat",
                    "Lemak: ": "0,8 - 1 gram per kg berat badan, Contoh: Berat 60Kg, 48-60 gram lemak/hari\n"
                               "Sumber Sehat: -Minyak zaitun 1 sdm ≈ 14 g lemak, -Alpukat 100 g ≈ 15 g lemak, -Kacang 30 g ≈ 14 g lemak",
                    "POLA MAKAN HARIAN BULKING: ": "-3 makan utama, -2 - 3 snack, -arak makan ±3 jam",
                    "Anjuran Dokter: ": "Latihan beban 3 - 5x per minggu agar kenaikan berat = otot, bukan lemak."
                }
            case "Normal":
                return{
                    "Kebutuhan Kalori: ": "Surplus Kalori: -> +300 sampai +500 kkal per hari dari kebutuhan normal(dokter tidak menyarankan lebih dari ini)",
                    "Takaran Makro Nutrisi(Per-hari): ": "Protein: 1,6-2,2 Gram per Kg berat badan, Contoh: Berat 60Kg, 96-132 gram protein/hari\n"
                                                         "Sumber & Takaran setara: -Dada ayam matang 100 g = ±31 g protein, -Telur utuh 1 butir = ±6 g protein, -Tempe 100 g = ±19 g protein, -Ikan 100 g = ±20-25 g protein\n"
                                                         "Karbohidrat: 4-6 gram per kg berat badan, Contoh: Berat 60Kg, 240-360 gram karbohidrat/hari\n"
                                                         "Sertara Makanan: -Nasi putih matang 100 g ≈ 28 g karbohidrat, -Kentang rebus 100 g ≈ 20 g karbohidrat, -Oatmeal kering 100 g ≈ 66 g karbohidrat",
                    "Lemak: ": "0,8 - 1 gram per kg berat badan, Contoh: Berat 60Kg, 48-60 gram lemak/hari\n"
                               "Sumber Sehat: -Minyak zaitun 1 sdm ≈ 14 g lemak, -Alpukat 100 g ≈ 15 g lemak, -Kacang 30 g ≈ 14 g lemak",
                    "POLA MAKAN HARIAN BULKING: ": "-3 makan utama, -2 - 3 snack, -arak makan ±3 jam",
                    "Anjuran Dokter: ": "Latihan beban 3 - 5x per minggu agar kenaikan berat = otot, bukan lemak."
                }

    def cutting(self):
        _,kategori = self.menghitungbb()
        match kategori:
            case "Normal":
                {
                    "Kebutuhan Kalori: ": "Defisit Kalori: -> -300 sampai -500 kkal per hari\n"
                                          "Penurunan Aman: 0,5 - 1 kg per minggu",
                    "Takaran Makro Nutrisi(Per-hari): ": "Protein(Paling Penting): 2-2,4 Gram per Kg berat badan, Contoh: Berat 70Kg, 140-168 gram protein/hari\n"
                                                         "Sumber & Takaran setara: -Dada ayam matang 100 g = ±31 g protein, -Telur utuh 1 butir = ±6 g protein, -Tempe 100 g = ±19 g protein, -Ikan 100 g = ±20-25 g protein, -Greek yoghurt plain 100 g = 10 g protein\n"
                                                         "Karbohidrat: 2-3 gram per kg berat badan, Contoh: Berat 70Kg, 140-210 gram karbohidrat/hari\n"
                                                         "Sertara Makanan: -Nasi putih matang 100 g ≈ 28 g karbohidrat, -Kentang rebus 100 g ≈ 20 g karbohidrat, -Oatmeal kering 40 g ≈ 26 g karbohidrat, -Roti gandum 1 lembar ≈ 15 g karbohidrat, -Nasi merah matang 100 g ≈ 23 g karbohidrat",
                    "Lemak: ": "0,5 - 0,8 gram per kg berat badan, Contoh: Berat 70Kg, 35-56 gram lemak/hari\n"
                               "Sumber Takaran Setara: -Minyak zaitun 1 sdm ≈ 14 g lemak, -Alpukat 100 g ≈ 15 g lemak, -Kacang Almond 30 g ≈ 14 g lemak, -Ikan berlemak 100 g ≈ 10 - 12 g lemak",
                    "Sayuran(Wajib, Bebas Kalori Rendah): ": "Bayam, Brokoli, Kol, Buncis",
                    "Pola Makan Harian Cutting: ": "-3 makan utama, -1 - 2 snack tinggi protein, -Air Putih 2-3L / hari",
                    "Larangan Saat Cutting: ": "-Minuman manis & soda, -Gorengan, -Fast food, -Gula berlebihan",
                    "Catatan Medis: ": "-Jika pusing, lemas ekstrem, atau berat turun terlalu cepat -> kalori terlalu rendah, -Kondisi khusus (diabetes, ginjal, asam urat) harus modifikasi dokter",
                    "Anjuran Dokter: ": "Protein: -Protein dibagi rata di setiap waktu makan, -Dianjurkan 20 - 40 g protein per makan. Karbohidrat: -Karbohidrat dikonsumsi pagi & siang, -Kurangi karbohidrat malam hari bila tidak latihan. Lemak: -Lemak tetap diperlukan untuk hormon, -Jangan kurang dari 0,5 g/kg BB"
                }
            case "Berat Badan Berlebih":
                {
                    "Kebutuhan Kalori: ": "Defisit Kalori: -> -300 sampai -500 kkal per hari\n"
                                          "Penurunan Aman: 0,5 - 1 kg per minggu",
                    "Takaran Makro Nutrisi(Per-hari): ": "Protein(Paling Penting): 2-2,4 Gram per Kg berat badan, Contoh: Berat 70Kg, 140-168 gram protein/hari\n"
                                                         "Sumber & Takaran setara: -Dada ayam matang 100 g = ±31 g protein, -Telur utuh 1 butir = ±6 g protein, -Tempe 100 g = ±19 g protein, -Ikan 100 g = ±20-25 g protein, -Greek yoghurt plain 100 g = 10 g protein\n"
                                                         "Karbohidrat: 2-3 gram per kg berat badan, Contoh: Berat 70Kg, 140-210 gram karbohidrat/hari\n"
                                                         "Sertara Makanan: -Nasi putih matang 100 g ≈ 28 g karbohidrat, -Kentang rebus 100 g ≈ 20 g karbohidrat, -Oatmeal kering 40 g ≈ 26 g karbohidrat, -Roti gandum 1 lembar ≈ 15 g karbohidrat, -Nasi merah matang 100 g ≈ 23 g karbohidrat",
                    "Lemak: ": "0,5 - 0,8 gram per kg berat badan, Contoh: Berat 70Kg, 35-56 gram lemak/hari\n"
                               "Sumber Takaran Setara: -Minyak zaitun 1 sdm ≈ 14 g lemak, -Alpukat 100 g ≈ 15 g lemak, -Kacang Almond 30 g ≈ 14 g lemak, -Ikan berlemak 100 g ≈ 10 - 12 g lemak",
                    "Sayuran(Wajib, Bebas Kalori Rendah): ": "Bayam, Brokoli, Kol, Buncis",
                    "Pola Makan Harian Cutting: ": "-3 makan utama, -1 - 2 snack tinggi protein, -Air Putih 2-3L / hari",
                    "Larangan Saat Cutting: ": "-Minuman manis & soda, -Gorengan, -Fast food, -Gula berlebihan",
                    "Catatan Medis: ": "-Jika pusing, lemas ekstrem, atau berat turun terlalu cepat -> kalori terlalu rendah, -Kondisi khusus (diabetes, ginjal, asam urat) harus modifikasi dokter",
                    "Anjuran Dokter: ": "Protein: -Protein dibagi rata di setiap waktu makan, -Dianjurkan 20 - 40 g protein per makan. Karbohidrat: -Karbohidrat dikonsumsi pagi & siang, -Kurangi karbohidrat malam hari bila tidak latihan. Lemak: -Lemak tetap diperlukan untuk hormon, -Jangan kurang dari 0,5 g/kg BB"
                }
            case "Obesitas":
                {
                    "Kebutuhan Kalori: ": "Defisit Kalori: -> -300 sampai -500 kkal per hari\n"
                                          "Penurunan Aman: 0,5 - 1 kg per minggu",
                    "Takaran Makro Nutrisi(Per-hari): ": "Protein(Paling Penting): 2-2,4 Gram per Kg berat badan, Contoh: Berat 70Kg, 140-168 gram protein/hari\n"
                                                         "Sumber & Takaran setara: -Dada ayam matang 100 g = ±31 g protein, -Telur utuh 1 butir = ±6 g protein, -Tempe 100 g = ±19 g protein, -Ikan 100 g = ±20-25 g protein, -Greek yoghurt plain 100 g = 10 g protein\n"
                                                         "Karbohidrat: 2-3 gram per kg berat badan, Contoh: Berat 70Kg, 140-210 gram karbohidrat/hari\n"
                                                         "Sertara Makanan: -Nasi putih matang 100 g ≈ 28 g karbohidrat, -Kentang rebus 100 g ≈ 20 g karbohidrat, -Oatmeal kering 40 g ≈ 26 g karbohidrat, -Roti gandum 1 lembar ≈ 15 g karbohidrat, -Nasi merah matang 100 g ≈ 23 g karbohidrat",
                    "Lemak: ": "0,5 - 0,8 gram per kg berat badan, Contoh: Berat 70Kg, 35-56 gram lemak/hari\n"
                               "Sumber Takaran Setara: -Minyak zaitun 1 sdm ≈ 14 g lemak, -Alpukat 100 g ≈ 15 g lemak, -Kacang Almond 30 g ≈ 14 g lemak, -Ikan berlemak 100 g ≈ 10 - 12 g lemak",
                    "Sayuran(Wajib, Bebas Kalori Rendah): ": "Bayam, Brokoli, Kol, Buncis",
                    "Pola Makan Harian Cutting: ": "-3 makan utama, -1 - 2 snack tinggi protein, -Air Putih 2-3L / hari",
                    "Larangan Saat Cutting: ": "-Minuman manis & soda, -Gorengan, -Fast food, -Gula berlebihan",
                    "Catatan Medis: ": "-Jika pusing, lemas ekstrem, atau berat turun terlalu cepat -> kalori terlalu rendah, -Kondisi khusus (diabetes, ginjal, asam urat) harus modifikasi dokter",
                    "Anjuran Dokter: ": "Protein: -Protein dibagi rata di setiap waktu makan, -Dianjurkan 20 - 40 g protein per makan. Karbohidrat: -Karbohidrat dikonsumsi pagi & siang, -Kurangi karbohidrat malam hari bila tidak latihan. Lemak: -Lemak tetap diperlukan untuk hormon, -Jangan kurang dari 0,5 g/kg BB"
                }