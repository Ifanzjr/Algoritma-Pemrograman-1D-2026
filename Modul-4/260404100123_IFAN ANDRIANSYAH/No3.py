n = int(input("masukkan bilangan : "))

for i in range (1, n + 1): 

    for j in range (1, i + 1):
        print (j, end="")

    for a in range (n-i)  :
        print (" ", end=" ")

    for k in range (i, 0, -1):
        print (k, end="")   

    print()  