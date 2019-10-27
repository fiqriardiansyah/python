#system pengelolaan data mahasiswa

'''


made by : fiqri ardiansyah

program ini merupakan pengelolaan array yang mempunyai fitur menambahkan,
menghapus, mengubah dan melihat isi array



'''

#function
#saya membuat function sendiri karna function ini akan dipanggil berulang kali.

    #function ini bertujuan untuk menggabungkan array yang terpisah dan concate
    #dengan tanda _
def concKalimat(jb):
    concate = ""
    for i in range(len(jb)):
        if i == len(jb)-1:
            concate += jb[i]
        else:
            concate += jb[i] + "_"
    return concate




#main
namaSiswa = []
nimSiswa = []
jurusanSiswa = []


stop1 = True
while stop1:

    print()
    print("====== system pengelolaan data mahasiswa ======")
    print()
    print("[1] tambah data \n[2] lihat daftar \n[3] hapus \n[4] ubah \n[5] keluar")
    act = input("pilih 1,2,3,4,5 > ")
    print()

    #jika user ingin menambah array
    if act == "1":
        print()
        print("====== tambah data ======")
        nama = input("nama siswa : ").split()
        nim = input("nim siswa : ").split()
        jur = input("jurusan : ").split()
        
        #inputan akan dimasukkan ke array masing2
        namaSiswa += concKalimat(nama).split()
        nimSiswa += concKalimat(nim).split()
        jurusanSiswa += concKalimat(jur).split()

        print("data berhasil ditambah !")
        
        #blok perulangan jika user ingin menambahkan data lagi
        stop  = True
        while stop:
            ty = input("tambah data lagi ? [y/t]")
            
            if ty == "y":
                nama = input("nama siswa : ").split()
                nim = input("nim siswa : ").split()
                jur = input("jurusan : ").split()

                namaSiswa += concKalimat(nama).split()
                nimSiswa += concKalimat(nim).split()
                jurusanSiswa += concKalimat(jur).split()
                
            elif ty == "t":
                print("-- gagal menambahkan !")
                print("-- silahkan pilih menu lain !!")
                #menghentikan perulangaan
                stop = False
            else:
                print("inputan salah")

    #jika user ingin melihat isi array
    elif act == "2":
        if len(namaSiswa) == 0:
            print("- daftar kosong ! silahkan tambah data terlebih dahulu")
        else:
            #melakukan perulangan untuk menampilkan array
            print()
            print("========== daftar mahasiswa =========")
            for i in range(len(namaSiswa)):
                print("%i. %s   %s    %s"%(i+1,namaSiswa[i],nimSiswa[i],jurusanSiswa[i]))

    #jika user ingin menghapus array
    elif act == "3":
        if len(namaSiswa) == 0:
            print("- daftar kosong ! silahkan tambah data terlebih dahulu")
        else:
            print()
            print("========== hapus mahasiswa =========")
            print()
            #menampilkan isi array terlebih dahulu
            for i in range(len(namaSiswa)):
                print("%i. %s   %s    %s"%(i+1,namaSiswa[i],nimSiswa[i],jurusanSiswa[i]))
            #pilih index array 
            hps = int(input("pilih nomor : "))
            #jika index tidak ada
            if len(namaSiswa) < hps:
                print("nomor mahasiswa tidak ditemukan ")
            else:
                namaSiswa[hps-1:hps]=[]
                nimSiswa[hps-1:hps]=[]
                jurusanSiswa[hps-1:hps]=[]
                print("- data berhasil dihapus!")


    #jika user ingin mengubah isi array
    elif act == "4":
        #cek jika array kosong
        if len(namaSiswa) == 0:
            print("- daftar kosong ! silahkan tambah data terlebih dahulu")
        else:
            print()
            print("========== daftar mahasiswa =========")
            for i in range(len(namaSiswa)):
                print("%i. %s   %s    %s"%(i+1,namaSiswa[i],nimSiswa[i],jurusanSiswa[i]))
            print()
            print("============ubah data ==============")
            ubh = int(input("nomor mahasiswa :"))
            if len(namaSiswa) < ubh:
                print("nomor mahasiswa tidak ditemukan !")
            else:  
                nama = input("nama siswa : ").split()
                nim = input("nim siswa : ").split()
                jur = input("jurusan : ").split()

                namaSiswa[ubh-1:ubh]=[concKalimat(nama)]
                nimSiswa[ubh-1:ubh]=[concKalimat(nim)]
                jurusanSiswa[ubh-1:ubh]=[concKalimat(jur)]
                print(ubh)
                print("- data berhasil diubah!")
    elif act == "5":
        print("=====================")
        print("----terimakasih !----")
        print("=====================")
        stop1 = False
    else:
        print("perintah tidak ditemukan!")

                
            

            
            
        
        

    
    

