#menuliskan daftar belanja

'''

made by : fiqri ardiansyah


program ini merupakan pengelolaan array sederhana yang hanya ada fitur
menambahkan isi array dan melihat isi array
'''
print("============== menuliskan daftar belanja ============")
print()

daftar = []
harga = []
total = 0

stop = True
while stop:
    if len(daftar) == 0:
        print("daftar belanja kosong")
        conf = input("- isi daftar ? [y/t]")
        if conf == "y":
            isi = input("belanjaan : ").split()
            hargabrg = input("harga : ").split()
            daftar += isi
            harga += hargabrg
            print()
            print("daftar belanja : ")
            for i in range(len(daftar)):
                print(" - %s : %s"%(daftar[i],harga[i]))
            print()
            #perulangan akan berhenti jika user menginputkan t
            while stop:
                confir = input("- isi daftar lagi ? [y/t]")
                if confir == "y":
                    belnj = input("belanjaan : ").split()
                    hrg = input("harga : ").split()
                    daftar += belnj
                    harga += hrg
                elif confir == "t":
                    print()
                    print("daftar belanja : ")
                    for i in range(len(daftar)):
                        print(" - %s : %s"%(daftar[i],harga[i]))
                    print()

                    for i in harga:
                        total += int(i)
                    print("Total  : %i"%(total)) 
                    
                    print("terimakasih!")
                    stop = False
                else:
                    print("input tidak ada")
            stop = False
        elif conf == "t":
            print("terimakasih")
            stop = False
        else:
            print("inputan salah")
            print()

    
    
