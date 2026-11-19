tugas = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. tambah tugas")
    print("2. tampilkan semua tugas")
    print("3. tandai tugas selesai")
    print("4. hapus tugas")
    print("5. jumlah tugas selesai & belum")
    print("6. keluar")
    pilih = input("pilih menu: ")

    if pilih == "1":
        nama = input("nama tugas: ")
        if nama in tugas:
            print("tugas sudah ada")
        else:
            tugas[nama] = "belum"
            print("tugas ditambahkan.")

    elif pilih == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            for nama in tugas:
                print("-", nama, ":", tugas[nama])

    elif pilih == "3":
        nama = input("nama tugas yang selesai: ")
        if nama in tugas:
            tugas[nama] = "selesai"
            print("tugas ditandai selesai.")
        else:
            print("tugas tidak ditemukan!")

    elif pilih == "4":
        nama = input("nama tugas yang dihapus: ")
        if nama in tugas:
            del tugas[nama]
            print("tugas dihapus.")
        else:
            print("tugas tidak ditemukan!")

    elif pilih == "5":
        selesai = 0
        belum = 0
        for nama in tugas:
            if tugas[nama] == "selesai":
                selesai += 1
            else:
                belum += 1
        print("tugas selesai:", selesai)
        print("tugas belum selesai:", belum)

    elif pilih == "6":
        print("terima kasih!")
        break

    else:
        print("menu tidak valid!")   