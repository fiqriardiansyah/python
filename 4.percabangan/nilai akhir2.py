#perbangan

'''

made by : fiqri ardiansyah


menentukan nilai akhir dari mahasiswa
masukan =   -nilai tugas (berupa angka integer 1-100)
            -nilai uas (berupa angka integer 1-100)
            -nilai uts (berupa angka integer 1-100)
dan akan mengeluarkan nilai 
'''


print("====== menentukan nilai akhir semester =====")
print()

n_tugas = int(input("nilai tugas : "))
n_uts = int(input("nilai uts : "))
n_uas = int(input("nilai uas : "))


tugas = n_tugas * 0.3
uts = n_uts * 0.3
uas = n_uas * 0.4

hasil = tugas + uts + uas

if hasil >= 90 and hasil <= 100:
    nilai = "A+"
elif hasil >= 80 and hasil <90:
    nilai = "A-"
elif hasil >= 70 and hasil <80:
    nilai = "B+"
elif hasil >= 60 and hasil <70:
    nilai = "B-"
elif hasil >= 50 and hasil <60:
    nilai = "C+"
elif hasil >= 40 and hasil <50:
    nilai = "C-"
else:
    nilai = "D"

print("nilai akhir anda : ",nilai)
