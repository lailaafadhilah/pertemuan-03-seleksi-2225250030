# Latihan 4 Pertemuan 03
# Menentukan Jenis Segitiga
# Nama: Laila Fadhilah
# NIM: 2225250030
# Kelas: 3A

# Input
sisi1 = float(input("Masukkan sisi pertama: "))
sisi2 = float(input("Masukkan sisi kedua: "))
sisi3 = float(input("Masukkan sisi ketiga: "))

# Proses dan keputusan
if sisi1 + sisi2 > sisi3 and sisi1 + sisi3 > sisi2 and sisi2 + sisi3 > sisi1:
    if sisi1 == sisi2 and sisi2 == sisi3:
        print("Segitiga sama sisi.")
    else:
        if sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
            print("Segitiga sama kaki.")
        else:
            print("Segitiga sembarang.")
else:
    print("Bukan segitiga yang valid.")