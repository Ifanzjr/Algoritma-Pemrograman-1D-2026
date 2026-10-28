baris = int (input("masukkan baris :"))
lampu = int (input("jumlah lampu tiap baris : "))

for i in range (1, baris + 1):
    for j in range (1, lampu + 1):
        if j % 3 == 0:
            print ("baris", i, "lampu", j, "gangguan")
        else :
            print("baris", i, "lampu", j, "normal")
print ("periksa sumber listrik utama taman ")