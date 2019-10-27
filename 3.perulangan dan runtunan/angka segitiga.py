#perulangan

'''

made by : fiqri ardiansyah

perulangan ini akan menghasilkan bentuk segitiga yang akan berulang
masukan = sebuah angka (integer) boleh berapa saja ,tetapi agar bentuk segitiga
terlihat maka angka yang nilainya kecil
'''

nilai = int(input("angka rentang 1-20 : "))

n = nilai+1



while n != 1:
    for i in range(0,n):
        for j in range(i+1,n):
            print(j,end=" ")
        print()
    for i in range(n,1,-1):
        for j in range(i-1,n):
            print(j,end=" ")
        print()
    n -= 1
