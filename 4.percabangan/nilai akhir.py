#melihat nilai akhir mahasiswa

'''
made by : fiqri ardiansyah


melihat nilai akhir dari mahasiswa yang sudah ada di daftar dengan
memasukkan nim yang sudah terdaftar ,maka program akan mengecek nim yang
diinputkan dengan yang sudah terdaftar jika ada akan mennampilkan muncul 2
pilihan yaitu nilai uts dan nilai uas

'''

print("===== melihat nili akhir mahasiswa =====")
print()
print("==============================================================")
print("no |      nama    |    nim     |     jurusan   |      kelas   ")
print("==============================================================")
print(" 1   fiqri          191111827     T informatika     scb sore")
print(" 2   aldi           192222222     T informatika     scb pagi")
print(" 3   nur            180909090     S informasi       sca sore")
print(" 4   lela           129999999     T informatika     scb sore")
print("==============================================================")
nim = input("masukkan nim siswa :")

if nim == "191111827":
    print("[1] nilai uts \n[2] nilai uas")
    tnya = input("lihat nilai no : [1,2]")
    if tnya == "1":
        print("nilai uts fiqri : 90")
    elif tnya == "2":
        print("nilai uas fiqri : 98")
    else:
        print("inputan tidak ada")
elif nim == "19222222":
    print("[1] nilai uts \n[2] nilai uas")
    tnya = input("lihat nilai no : [1,2]")
    if tnya == "1":
        print("nilai uts aldi : 100")
    elif tnya == "2":
        print("nilai uas aldi : 88")
    else:
        print("inputan tidak ada")
elif nim == "180909090":
    print("[1] nilai uts \n[2] nilai uas")
    tnya = input("lihat nilai no : [1,2]")
    if tnya == "1":
        print("nilai uts nur : 70")
    elif tnya == "2":
        print("nilai uas nur : 70")
    else:
        print("inputan tidak ada")
elif nim == "129999999":
    print("[1] nilai uts \n[2] nilai uas")
    tnya = input("lihat nilai no : [1,2]")
    if tnya == "1":
        print("nilai uts lela : 90")
    elif tnya == "2":
        print("nilai uas lela : 90")
    else:
        print("inputan tidak ada")
else:
    print("inputan tidak ada")
