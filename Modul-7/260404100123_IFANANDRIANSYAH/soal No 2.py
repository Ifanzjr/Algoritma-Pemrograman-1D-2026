playlist = {}

while True:
    print("\n=== MENU PLAYLIST ===")
    print("1. buat playlist")
    print("2. tambah lagu ke playlist")
    print("3. tampilkan semua playlist")
    print("4. cari lagu")
    print("5. hapus lagu dari playlist")
    print("6. hapus playlist")
    print("7. keluar")
    pilih = input("pilih menu: ")

    if pilih == "1":
        nama = input("nama playlist: ")
        if nama in playlist:
            print("playlist sudah ada!")
        else:
            playlist[nama] = {}
            print("playlist dibuat.")

    elif pilih == "2":
        nama = input("nama playlist: ")
        if nama in playlist:
            judul = input("judul lagu: ")
            penyanyi = input("penyanyi: ")
            playlist[nama][judul] = penyanyi
            print("lagu ditambahkan.")
        else:
            print("playlist tidak ditemukan!")

    elif pilih == "3":
        if len(playlist) == 0:
            print("belum ada playlist.")
        else:
            for nama in playlist:
                print("Playlist:", nama)
                if len(playlist[nama]) == 0:
                    print("  (kosong)")
                else:
                    for judul in playlist[nama]:
                        print("  -", judul, "by", playlist[nama][judul])

    elif pilih == "4":
        cari = input("judul lagu yang dicari: ")
        ketemu = False
        for nama in playlist:
            if cari in playlist[nama]:
                print("ditemukan di playlist", nama, "- Penyanyi:", playlist[nama][cari])
                ketemu = True
        if not ketemu:
            print("Lagu tidak ditemukan!")

    elif pilih == "5":
        nama = input("nama playlist: ")
        if nama in playlist:
            judul = input("judul lagu yang dihapus: ")
            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("lagu dihapus.")
            else:
                print("lagu tidak ditemukan")
        else:
            print("playlist tidak ditemukan")

    elif pilih == "6":
        nama = input("nama playlist yang dihapus: ")
        if nama in playlist:
            del playlist[nama]
            print("playlist dihapus.")
        else:
            print("playlist tidak ditemukan!")

    elif pilih == "7":
        print("terima kasih!")
        break
        
    else:
        print("menu tidak valid!")