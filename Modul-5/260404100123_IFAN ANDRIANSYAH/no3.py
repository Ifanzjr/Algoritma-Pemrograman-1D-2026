def hitungNilai (nama, tugas, UTS, UAS ):
    nilaiAkhir = (tugas * 0.30) + (UTS * 0.30) + (UAS * 0.40)

    if nilaiAkhir >= 85:
        grade = "A"
    elif nilaiAkhir >= 70 :
        grade = "B"
    elif nilaiAkhir >= 55:
        grade = "C"
    else:
        grade = "D"

    if grade == "D":
        status = "tidak lulus"
    else:
        status = "lulus"

    print("nama     :", nama)
    print ("tugas    :", tugas )
    print("UTS      :", UTS)
    print("UAS      :", UAS)
    print("nilaiAkhir   :", nilaiAkhir)
    print("grade    :", grade)
    print("status     :" ,status )

nama = input("masukkan nama mahasiswa  : ")
tugas = float(input("masukkan nilai tugas  :"))
UTS = float (input (" masukkan nilai UTS    :"))
UAS = float (input( " masukkan nilai UAS    :"))
hitungNilai (nama, tugas , UTS, UAS )
