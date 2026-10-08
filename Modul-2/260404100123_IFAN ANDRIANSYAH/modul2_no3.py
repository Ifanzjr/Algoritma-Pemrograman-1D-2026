suhu = int (input("masukkan suhu tekanan reaktor : "))
tekanan = int (input("masukkan tekanan gas: "))
print (suhu)
print (tekanan)
if suhu > 1000 :
    if tekanan > 50:
        print ("SEGERA EVAKUASI :")
    else: 
        print ("bahaya suhu : segera turunkan daya !")
elif suhu > 500:
    if tekanan > 30:
        print ("tekanan tidak stabil ")
    else:
        print ("operasi reaktor normal")
else :
    print ("reaktor belum cukup panas ")
pompa = "pompa maksimal" if suhu > 800 else "pompa normal"
print (pompa)