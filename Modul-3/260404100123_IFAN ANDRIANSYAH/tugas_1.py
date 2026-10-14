jumlahPenumpang = 0
totalPendapatan = 0
jarakTerjauh = 0
totalJarak = 0

print("=== Kasir Terminal Bus Sidoarjo ===")

while True:
    jarak = int(input("Masukkan jarak tempuh (km) "))

    if jarak == 0:
        break

    if jarak < 0:
        print("Jarak tidak valid, silakan masukkan lagi")
        continue
    jumlahPenumpang += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlahPenumpang % 5 == 0:
        tarif = tarif * 0.5
        print("Penumpang ke-%d mendapat diskon 50//" % jumlahPenumpang)
    print("Tarif penumpang ke-%d : Rp%d" % (jumlahPenumpang, tarif))

    totalPendapatan += tarif
    totalJarak += jarak

    if jarak > jarakTerjauh:
        jarakTerjauh = jarak

print("\n=== Rekap Hari Ini ===")
print("Jumlah penumpang :", jumlahPenumpang)
print("Total pendapatan : Rp%d" % totalPendapatan)

if jumlahPenumpang > 0:
    rata_rata = totalJarak / jumlahPenumpang
    print("Jarak terjauh    :", jarakTerjauh, "km")
    print("Rata-rata jarak  : %.2f km" % rata_rata)
else:
    print("Belum ada penumpang yang tercatat")