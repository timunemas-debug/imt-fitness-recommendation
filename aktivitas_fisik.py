from beratbadan import BeratBadan

class AktivitasFisik(BeratBadan):
    def __init__(self, berat_badan, tinggi_badan, jenis_kelamin):
        super().__init__(berat_badan, tinggi_badan, jenis_kelamin)
    
    def aktivitas_ringan(self):
        _,kategori = self.menghitungbb()
        match kategori:
            case "Normal":
                return{
                    "Aktivitas": "1. Kardio sedang (jogging, skipping, bersepeda)\n"
                                 "2.Olahraga tim (basket, futsal, bulu tangkis)\n"
                                 "3.Latihan kekuatan tubuh",
                    "Durasi": "40 - 60 menit, 4 - 5x/Minggu"
                }
            case "Kurus":
                return{
                    "Aktivitas": "1. Latihan kekuatan ringan - sedang (squat, push-up, plank, resistance band)\n"
                                 "2. Olahraga ringan menyenangkan (berenang santai, bersepeda ringan)\n"
                                 "3. Peregangan & yoga",
                    "Durasi": "30 - 45 menit, 3 - 4x/Minggu"
                }
            case "Berat Badan Berlebih":
                return{
                    "Aktivitas": "1.Kardio berdampak rendah (jalan cepat, sepeda, berenang)\n"
                                 "2. Senam, dance, atau zumba remaja\n"
                                 "3. Latihan kekuatan ringan",
                    "Durasi": "45 - 60 menit, 5x/Minggu",
                    "Peringatan": "Hindari lari atau lompat berlebihan di awal!!!"
                }
            case "Obesitas":
                return{
                    "Aktivitas": "1. Jalan santai -> jalan cepat (bertahap)\n"
                                 "2. Berenang atau bersepeda statis\n"
                                 "3. Latihan duduk-berdiri & peregangan",
                    "Durasi": "Mulai 20 - 30 menit, naik bertahap, 5 - 6x/Minggu",
                    "Peringatan": "Fokus konsistensi, bukan intensitas"
                }
            
    def membangun_masa_otot(self):
        _,kategori = self.menghitungbb()
        match kategori:
            case "Normal":
                return{
                    "Fokus Utama": "Body Recomposition(Otot Naik, Lemak Terkontrol)",
                    "Jenis latihan": "Latihan beban -> Wajib",
                    "Frekuensi": "3-5x per minggu",
                    "Split latihan": "Hari 1: Upper/Lower\n"
                                     "Hari 2: Push/Pull/Legs\n"
                                     "Hari 3: Full body(3x/minggu)",
                    "Contoh Latihan Inti": "Squat/Leg press,Bench press, Deadlift, Pull-up, Shoulder press",
                    "Set & Repetisi": "3-5 Set\n"
                                      "6-12 Repetisi\n"
                                      "Progressive overload(Beban naik bertahap)"
                }
            case "Kurus":
                return{
                    "Fokus Utama": "Menambah Massa Otot(Bulking Terkontrol)",
                    "Jenis latihan": "Resistence",
                    "Frekuensi": "3-4x per minggu",
                    "Split latihan": "Hari 1: Upper body\n"
                                     "Hari 2: Lower body\n"
                                     "Hari 3: Full body",
                    "Contoh Latihan Inti": "Squat,Bench press, Deadlift, Pull-up, Solder press",
                    "Set & Repetisi": "3-5 Set\n"
                                      "6-12 Repetisi\n"
                                      "Progressive overload(Beban naik bertahap)"
                }
            case "Berat Badan Berlebih":
                return{
                    "Fokus Utama": "Turunkan Lemak Sambil Membangun Massa Otot(Lean Recomp/Cut Ringan)",
                    "Jenis latihan": "Resistance Training -> Wajib",
                    "Frekuensi": "3-4x per minggu",
                    "Split latihan": "Hari 1: Upper body\n"
                                     "Hari 2: Lower body\n"
                                     "Hari 3: Full body",
                    "Contoh Latihan Inti": "Squat,Bench press, Deadlift/Hip hinge, Pull-up/Lat pulldown, Solder press",
                    "Set & Repetisi": "3-4 Set\n"
                                      "8-12 Repetisi\n"
                                      "Progressive overload(Beban naik bertahap)"
                }
            case "Obesitas":
                return{
                    "Fokus Utama": "Menurunkan Lemak Dan Menjaga Massa Otot",
                    "Jenis latihan": "Resistance Training -> Wajib\n"
                                     "Cardio berlebihan -> Dihindari",
                    "Frekuensi": "3-4x per minggu",
                    "Split latihan": "Hari 1: Upper body\n"
                                     "Hari 2: Lower body\n"
                                     "Hari 3: Full body",
                    "Contoh Latihan Inti": "Squat,Bench press, Deadlift/Hip hinge Ringan, Pull-up/Lat pulldown, Solder press",
                    "Set & Repetisi": "2-4 Set\n"
                                      "8-12 Repetisi\n"
                                      "Progressive overload(Beban naik bertahap & Aman)"
                }
