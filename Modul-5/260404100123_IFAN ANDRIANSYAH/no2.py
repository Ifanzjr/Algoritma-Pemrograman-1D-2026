def cekPalindrom (kata):
    if kata == kata [:: - 1]:
         return True 
    else :
         return False

while True:
     kata = input("masukkan kata :")

     if kata == "selesai":
          break
     hasil = cekPalindrom(kata)
     print("hasil fungsi:", hasil)

     if hasil :
          print(f"{kata}: adalah palindrom")
     else:
          print(f"{kata}: bukan palindrom")     