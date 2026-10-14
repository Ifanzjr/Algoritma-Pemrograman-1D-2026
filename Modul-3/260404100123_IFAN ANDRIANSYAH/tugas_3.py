jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0

totalNilai = 0
tertinggi = -1
terendah = 101
namaTertinggi = ""
namaTerendah = ""

for i in range(1, 11):
    print("--- Mahasiswa ke-%d ---" % i)
    nama = input("Nama : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if akhir >= 85: 
        kategori = "A"
        jumlah_a += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1
    print("Hasil -> %s | Tugas: %.0f | UTS: %.0f | UAS: %.0f | Akhir: %.2f | Kategori: %s"
          % (nama, tugas, uts, uas, akhir, kategori))
    totalNilai += akhir
    if akhir > tertinggi:
        tertinggi = akhir
        namaTertinggi = nama
    if akhir < terendah:
        terendah = akhir
        namaTerendah = nama
print("\n=== Rekap Kelas ===")
print("Jumlah nilai A :", jumlah_a)
print("Jumlah nilai B :", jumlah_b)
print("Jumlah nilai C :", jumlah_c)
print("Jumlah nilai D :", jumlah_d)
print("Jumlah nilai E :", jumlah_e)
print("Nilai tertinggi : %.2f (%s)" % (tertinggi, namaTertinggi))
print("Nilai terendah  : %.2f (%s)" % (terendah, namaTerendah))
print("Rata-rata kelas : %.2f" % (totalNilai / 10))