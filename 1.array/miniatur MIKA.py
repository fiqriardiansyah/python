#miniatur MIKA

'''

made by : fiqri ardiansyah


program ini merupakan pengelolaan array yang mempunyai fitur menambah, melihat dan mengubah
isi array yang dipadukan dengan perulangan dan percabangan

program ini bisa menampung banyak user yang bisa registrasi / membuat accout ,login , dan mengisi data

saya membuat function sendiri untuk menyingkat penulisan code dan agar program terlihat lebih rapi
'''

#FUNCTION

#function ini untuk menggabungkan 2 kata
#contoh isi parameter = ["fiqri","ardiansyah"]
#contoh return = "fiqri_ardiansyah"
def concKalimat(jb):
    concate = ""
    for i in range(len(jb)):
        if i == len(jb)-1:
            concate += jb[i]
        else:
            concate += jb[i] + " "
    return concate

#function ini untuk mengambil index array dari suatu data didalam array
#contoh isi parameter = "fiqri"
#contoh return = 3
def index(a):
    ind = 0
    for i in range(len(username)):
        if username[i] == a:
            ind += i
    return ind

#function ini untuk menampilkan seperti berikut agar code dibawah terlihat lebih rapi
def p():
    print("==================================")
    print("======== STMIK MIKROSKIL ========")
    print("==================================\n ")
    print("==================================")
    print("= ujian tengah semester (UTS) ======")
    print("= ganjil T.A 2019/2020 adalah 28 =====")
    print("= OKTOBER s/d 01 NOVEMBER 2019 ===")
    print("==================================")
    print()
    print("==========  LOGIN  ================")
    print()

#function ini untuk menampilkan nama siswa ,nim dan jurusan dari array sesuai index dari user yang login
#contoh isi parameter = "fiqri"
def tampilProfile(u):
    print("======== your profile ========")
    print("nama      : %s "%(nama_siswa[index(u)]))
    print("nim_siswa : %s "%(nim_siswa[index(u)]))
    print("jurusan   : %s "%(jur_siswa[index(u)]))
    print()
        
#function ini untuk menampilkan username dan password dari array sesuai index dari user yang login
#contoh isi parameter = "fiqi"
def tampilUserPas(u):
    print()
    print("your last username : ",username[index(u)])
    print("your last password : ",password[index(u)])
    print()

#function ini untuk mengecek apakah inputan dari user (username) sudah ada di dalam array atau belum jika sudah ada maka akan mengirim kan nilai false
#contoh isi parameter = "fiqri"
#contoh return = False
def cekUser(u):
    hasil = True
    for i in range(len(username)):
        if username[i] == concKalimat(u):
            hasil = False
    return hasil
            

#----------------------------------- MAIN PROGRAM ---------------------------------------
p()
#array penampung username dan password dari user
username = []
password = []

#array penampung data dari user
nama_siswa = []
jur_siswa = []
nim_siswa = []

stop = True
while stop:
    print("[1] login  \n[2] registrasi \n[3] exit")
    act = input("pilih 1,2,3 > ")

    #jika user memilih nomor 1 (login)
    if act == "1":
        print("\n =============== LOGIN ============\n")
        user = input("username : ")
        pas = input("password : ")

        #cek jika array username kosong maka user harus registrasi lebih dulu
        if len(username) == 0:
            print()
            print("- anda belum registrasi ! \n- silahkan registrasi \n")
        #jika ada maka : 
        else:
            #cek inputan user apakah inputan user sama dengan yang ada di array username
            if user == username[index(user)]:
                #cek inputan user apakah inputan user sama dengan yang ada di array username
                if pas  == password[index(user)]:
                    print()
                    print("====== welcome ",user," ======= \n ")
                    
                    stop3 = True
                    while stop3:
                        print("[1] lihat profile \n[2] edit profile \n[3] ubah password \n[4] logout")
                        print()
                        pro = input("pilih 1,2,3,4 > ")
                        print()
                
                        if pro == "1":
                            #function untuk menampilkan data user 
                            tampilProfile(user)
                        elif pro == "2":
                            print()
                            print("======== ubah data =======")
                            print()
                         
                            nama = input("ubah nama : ").split()
                            nim = input("ubah nim  : ").split()
                            jur = input("ubah jurusan :").split()
                            
                            #code dibawah untuk mengubah isi dari array sesuai index user
                            nama_siswa[index(user):index(user)+1]=[concKalimat(nama)]
                            nim_siswa[index(user):index(user)+1]=[concKalimat(nim)]
                            jur_siswa[index(user):index(user)+1]=[concKalimat(jur)]
                            
                            print()
                            print("- data berhasil diubah !")
                            print()

                        elif pro == "3":
                            #menampilka username dan password user 
                            tampilUserPas(user)
                            pas = input("your new password : ").split()
                            #mengubah isi dari array sesuai index user
                            password[index(user):index(user)+1]=[concKalimat(pas)]
                            print()
                            print("your password has changed !")
                            print()
                        elif pro == "4":
                            print()
                            print("=== your have been logout !! ===\n")
                            #untuk menghentikan perulangan agar tidak kembali ke menu welcome dan kembali ke menu login
                            stop3 = False
                        else:
                            print()
                            print("-perintah tidak ada")

                else:
                    print("\n!!! password salah \n")
            else:
                print("\n!!! username salah \n")
            
    #jika user mau registrasi
    elif act == "2":

        stop4 = True
        while stop4:
            print()
            print("========= create account =========")
            print()
            
            user = input("username : ").split()
            nama = input("nama     : ").split()
            jur  = input("jurusan  : ").split()
            nim  = input("nim      : ").split()
            pas  = input("password : ").split()

            #cek terlebih dahulu apakah inputan user sudah ada atau belum di array username jika ada pengguna tidak boleh menambahkan user yang sama
            if cekUser(user):
                #jika tidak ada maka semua inputan akan ditambah kan ke array masing2
                nama_siswa += concKalimat(nama).split()
                nim_siswa += concKalimat(nim).split()
                jur_siswa += concKalimat(jur).split()
                username += concKalimat(user).split()
                password += concKalimat(pas).split()

                print()
                print("- congrats! account has create !")
                print(" ------ SILAHKAN LOGIN -------- \n")
                stop4 = False
            else:
                #jika user sudah ada
                print("!!! username sudah terdaftar ")
        
        
    elif act == "3":
        #untuk menghentikan program
        print("-- terimakasih --")
        stop = False
    else:
        print("\n!!! perintah tidak ditemukan !!! \n")














