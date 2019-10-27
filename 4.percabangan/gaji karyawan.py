#percabangan

'''
made by : fiqri ardiansyah


meghitung gaji karyawan dengan cara menentukan gologan ,jam kerja dan jam lembur
hasil akhir adalah jam kerja dikali dengan golongan ditambah dengan jam lembur
dikali dengan banyak hari sebulan
masukan =   -pilih salah satu gologan karyawan
            -jumlah jam kerja dalam bentuk angka(integer)
            -jumlah jam lembur dalam bentuk angka(integer)

            
'''


print("====== menghitung gaji karyawan ========")
print()
golongan = input("pilih golongan : (A,B,C) ")
jamK = int(input("jumlah jam kerja perhari : (angka) "))
lembur = int(input("jumlah jam lembur : (angka) "))

A = 50000
B = 40000
C = 30000
lmbr = 50000
sebulan = 30

if golongan == "A":
    hari = (jamK * A) + (lembur * lmbr)
    hasil = "hasil gaji sebesar "+str(hari*sebulan)+" perbulan"
elif golongan == "B":
    hari = (jamK * A) + (lembur * lmbr)
    hasil = "hasil gaji sebesar "+str(hari*sebulan)+" perbulan"
elif golongan == "C":
    hari = (jamK * A) + (lembur * lmbr)
    hasil = "hasil gaji sebesar "+str(hari*sebulan)+" perbulan"
else:
    hasil = "golongan tidak ditemukan"

print(hasil)
