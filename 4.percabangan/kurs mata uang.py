#konversi kurs mata uang dari rupiah ke yang lain

'''

made by : fiqri ardiansyah


mengkonversikan rupiah ke mata uang lain
masukan = pilih salah satu mata uang dengan nomornya
            dan masukkan nominal dalam rupiah

'''




print("====== konversi kurs mata uang ======")
print("Dari rupiah Konversi ke : ")
print("[1] USD \n[2] YEN \n[3] PESSO")
dari = int(input("pilih 1,2,3, > "))

rupiah = int(input("Nominal Uang rupiah : "))

if dari == 1:
    hasil = str(rupiah/15000)+" USD"
elif dari == 2:
    hasil = str(rupiah/10000)+" YEN"
elif dari == 3:
    hasil = str(rupiah/5000)+" PESSO"
else:
    hasil = "pilihan tidak ada"
    
print(hasil)
    
