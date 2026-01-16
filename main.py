from beratbadan import BeratBadan
from aktivitas_fisik import AktivitasFisik
from nutrisi import Nutrisi
from userprofil import UserProfil

orang1 = BeratBadan(70, 176, "laki laki")
while True:
    print("=================================================")
    print("1. Menghitung Berat Badan  2. Rekomendasi Makanan")
    print("3. Rekomendasi Nutrisi     4. Bulking/Cutting")
    print("5. Pengaturan              6. Keluar")
    print("=================================================")
    user_input = input("Masukan Pilihan anda: ")
    match user_input:
        case "1":
            print(orang1.menghitungbb())
        case "2":
            print(orang1.rekomendasi_makanan())