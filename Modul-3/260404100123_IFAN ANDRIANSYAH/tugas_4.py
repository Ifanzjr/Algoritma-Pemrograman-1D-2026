beasiswaPenuh = 0
kuotaPenuh = 3

for i in range(1, 11):
    print("\n--- Mahasiswa ke-%d ---" % i)
    nama = input("Nama  : ")
    ipk = float(input("IPK   : "))
    penghasilan = int(input("Penghasilan orang tua   : "))

    if ipk < 3.00:
        print("%s tidak memenuhi syarat (IPK kurang dari 3,00)" % nama)
        continue

    if penghasilan <= 3000000:
        print("%s mendapat beasiswa penuh" % nama)
        beasiswaPenuh += 1
    elif penghasilan <= 5000000:
        print("%s mendapat beasiswa sebagian " % nama)
    else:
        print("%s tidak mendapat beasiswa (penghasilan orang tua terlalu tinggi)" % nama)
    if beasiswaPenuh == kuotaPenuh:
        print("\nKuota beasiswa penuh sudah terpenuhi, seleksi dihentikan")
        break
print("\nJumlah penerima beasiswa penuh:", beasiswaPenuh)