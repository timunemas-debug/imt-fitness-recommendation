from beratbadan import BeratBadan
from aktivitas_fisik import AktivitasFisik

orang1 = BeratBadan(30, 170, "Laki-laki")
orang2 = AktivitasFisik(30, 170, "Laki-laki")
imt, kategori = orang1.menghitungbb()
print(f"IMT: {imt}, Kategori: {kategori}")
print(f"{orang1.rekomendasi_makanan()}")
print(orang2.aktivitas_ringan())