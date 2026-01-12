tinggi_badan = int(input("TINGGI BADAN: ")) / 100
berat_badan = int(input("BERAT BADAN: "))

imt = berat_badan / (tinggi_badan**2)
print(round(imt, 2))