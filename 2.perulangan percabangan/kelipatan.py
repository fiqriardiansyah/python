#perulangan percabangan
'''
made by : fiqri ardiansyah

program ini akan menghasilkan kelipatan dari inputan (j) sampai batasnya adalah
inputan (n)
'''

n = int(input("kelipatan sampai : "))
j = int(input("kelipatan : "))

for i in range(1,n+1):
    if i % j == 0:
        print(i)
