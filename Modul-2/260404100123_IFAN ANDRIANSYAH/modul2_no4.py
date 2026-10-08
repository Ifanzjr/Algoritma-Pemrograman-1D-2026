pin = int (input("masukkan PIN 3 digit :"))
jam  = int (input ("masukkan jam kedatangan (0-23):"))
digit1 = pin //100
digit2 =(pin //10)%10
digit3 = pin%10
print(digit1)
print(digit2)
print(digit3)
if pin % 5 == 0:
    if jam < 12:
        print("garasi pagi terbuka")
    else :
        print ("garasi malam terbuka, lampu dinyalakan")
elif pin % 2 == 0:
    if digit1+digit3 == digit2:
        print ("garasi vip terbuka untuk bos ")
    else:
        print ("kode genap ditolak, alarm berbunyi")
else :
    print("akses ditolak")
cctv = "mode malam " if jam > 18 else "mode siang standbay"
print (cctv)
 