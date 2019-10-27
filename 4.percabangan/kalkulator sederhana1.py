#percabangan
'''

made by : fiqri ardiansyah

membuat kalkulator sederhana dengan menginputkan dua buah bilangan dan memilih
proses apa yang mau dikerjakan(penjumlahan,pengurangan,perkalian,pembagian)
'''

print("===== kalkulator sederhana 1 =====")
print()
print("[1] penjumlahan \n[2] pengurangan \n[3] perkalian \n[4] pembagian \n")
coose = int(input("pilih 1,2,3,4 : "))
angka1 = int(input("angka 1 : "))
angka2 = int(input("angka 2 : "))

hasil = ""
if coose == 1:
    hasil ="%i + %i = %i"%(angka1,angka2,angka1+angka2)
elif coose == 2:
    hasil = "%i - %i = %i"%(angka1,angka2,angka1-angka2)
elif coose == 3:
    hasil = "%i x %i = %i"%(angka1,angka2,angka1*angka2)
elif coose == 4:
    hasil ="%i : %i = %i"%(angka1,angka2,angka1/angka2)
else:
    hasil = "pilihan tidak ada"

print(hasil)
    
