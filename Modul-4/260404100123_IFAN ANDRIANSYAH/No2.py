total = 0
for i in range(1, 8):
    print("hari ke-", i)
    lembur= int(input("jam lembur :"))

    while lembur < 0 or lembur == 5 or lembur == 7 :
        print("jam lembur tidak sesuai ketentuan")
        lembur= int(input("masukkan ulang jam lembur: "))
    if lembur > 8:
        print("lembur melebihi batas")
        upahLembur = 0
    elif lembur <= 3:
        upahLembur = lembur * 25000
    elif lembur == 4:
        upahLembur = 100000
    elif lembur == 6:
        upahLembur = 200000
    else:
        upahLembur = 300000

    shift = input("shift malam? (y/t):")
    gaji = 100000 + upahLembur
    if shift == "y":
        gaji = gaji + 50000
    total = total + gaji
print("total gaji mingguan : Rp", total)