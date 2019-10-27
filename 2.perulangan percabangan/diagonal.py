#perulangan percabangan
'''

made by : fiqri ardiansyah

program ini akan menghasilkan deretan angka yang berderet secara diagonal
masukan = banyak bilangan disarankan tidak lebih dari 20 karna kalau
            lebih dari itu maka tampilan diagonal akan jelek
'''


bil = int(input("banyak bilangan : (disarankan tidak lebih dari 20) "))

while True:
    for i in range(1,bil+1):
        for j in range(1,bil+1):
            if i == j:
                print(i,end="    ")
            else:
                print(end="    ")
        print()

    for i in range(bil+1,0,-1):
        for j in range(1,bil+1):
            if i == j:
                print(i,end="    ")
            else:
                print(end="    ")
        print()
