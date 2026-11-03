def jumlahPelanggan(n):
    if n == 1 or n == 2:
        return 1

    return jumlahPelanggan (n-1) + jumlahPelanggan (n-2)
while True:
    teks= input(" masukkan hari ke N :")

    if teks == "selesai":
        break
    n = int(teks)

    if n < 1:
        print(" N  harus bilangan positif")
    else:
        print(f"jumlah hari ke - n : {jumlahPelanggan (n)}")