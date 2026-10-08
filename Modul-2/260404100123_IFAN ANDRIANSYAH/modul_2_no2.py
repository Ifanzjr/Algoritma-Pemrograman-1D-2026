totalBelanja = int (input("masukkan total belanja : Rp"))
if totalBelanja  % 100000 == 0: 
    totalBayar = 0
elif totalBelanja % 50000 == 0:
    totalBayar = totalBelanja  * 50//100
elif  totalBelanja % 10000 == 0:
    totalBayar = totalBelanja  * 20//100
elif totalBelanja >=200000 :
    totalBayar = totalBelanja  * 10//100
print ("total belanja awal : Rp", totalBelanja)
print ("total yang harus di bayar : Rp", totalBayar)
poin = ("point bertambah" if totalBayar > 0 else "tidak ada point") 
print (poin) 