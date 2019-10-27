#kalkulator sederhana 2
'''
made by : fiqri ardiansyah

program ini akan melakukan operasi matematika yaitu penjumlahan, pengurangan
perkalian dan pembagian dua digit
masukan = pilih dari keempat pilihan dan masukkan angka pertama dan angka
            kedua
'''

stop = True
while stop:
    print("===== kalkulator sederhana 2=====")
    print()
    print("[1] penjumlahan \n[2] pengurangan \n[3] perkalian \n[4] pembagian \n[5] keluar")
    coose = int(input("pilih 1,2,3,4 : "))
    

    hasil = ""
    if coose == 1:
        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))
        hasil ="%i + %i = %i"%(angka1,angka2,angka1+angka2)
    elif coose == 2:
        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))
        hasil = "%i - %i = %i"%(angka1,angka2,angka1-angka2)
    elif coose == 3:
        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))
        hasil = "%i x %i = %i"%(angka1,angka2,angka1*angka2)
    elif coose == 4:
        angka1 = int(input("angka 1 : "))
        angka2 = int(input("angka 2 : "))
        hasil ="%i : %i = %i"%(angka1,angka2,angka1/angka2)
    elif coose == 5:
        stop = False
        hasil = "terimakasih!!!"
    else:
        hasil = "inputan tidak ada"
    print(hasil)
    

