#perulangan 
'''
made by : fiqri ardiansyah

mencari nilai rata2 dari sebuah kumpulan nilai
masukan : kumpulan nilai
keluaran : 3 digit dibelakang koma
'''
nilai = input("kumpulan nilai : ").split()

hasil = 0

for i in nilai:
    hasil += int(i)
print("nilai rata2 : %.3f"%(hasil/len(nilai)))

