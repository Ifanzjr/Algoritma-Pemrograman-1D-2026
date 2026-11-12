temp =[]

while True:
    nama = input('masukkan nama asisten :')
    if nama == 'cukup':
        break
    temp.append(nama)
asistenAwal = tuple(temp)

tambahan = input("masukkan nama asisten tambahan :")
asistenAkhir = asistenAwal + (tambahan,)

temp =[]
while True:
    hari = input("masukkan hari tugas :")
    if hari == "cukup":
        break
    temp.append(hari)

hariTugas = tuple(temp)

asistenLibur = input ("nama asisten yang dikecualikan :")
hariLibur = input("hari yang dikecualikan :")

print("==jadwal shift==")
for asisten in asistenAkhir:
    for hari in hariTugas:
        if asisten == asistenLibur  and hari == hariLibur:
            continue
        print(asisten, "-", hari)
