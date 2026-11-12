def cekKelayakan(pc):
    ram = int(pc[2])
    if pc [1] == 'normal' and ram >= 8:
        return "layak"
    else:
        return "tidak layak"

dataPc = []
jumlah =int(input("jumlah PC yang akan di data :"))

for i in range (jumlah):
    print ("PC ke -" + str (i + 1))
    nama = input ("nama PC :")
    status = input ("status (normal/rusak): ")
    ram = input ("kapasitas RAM (GB): ")
    dataPc.append ([nama, status, ram])

print("== hasil evaluasi ==")
for pc in dataPc :
    try:
        hasil = cekKelayakan(pc)
    except ValueError:
        hasil = "format RAM kacau"

    print('{"PC":" ' + pc[0] + ' ", "status": " ' + hasil + ' "}')