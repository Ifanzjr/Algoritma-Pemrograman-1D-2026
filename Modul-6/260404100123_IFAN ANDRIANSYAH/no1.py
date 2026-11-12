daftar = []

while True:
    nama = input ('masukkan  nama calon anggota :')
    if nama == "selesai":
        break 
    daftar.append(nama)

print('== hasil akhir ==')
for nama in daftar:
    if nama == 'admin' or len(nama) <4:
        print(nama, "nama tidak valid")
    else:
        print(nama, "valid")

penyusup = input ('masukkan nama yang dicurigai sebagai penyusup :')
if penyusup in daftar :
    daftar.remove(penyusup)
    print(penyusup, "berhasil di hapus")
else:
    print("nama", penyusup, "tidak di temukan di pendaftaran")

print("daftar terakhir", daftar)