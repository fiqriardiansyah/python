#system pengelolaan buku 2
'''

made by : fiqri ardiansyah


program ini merupakan program penglolaaan array sederhana yang mempunyai
fitur menambahkan , menghapus,mengubah dan melihat isi array
'''



#saya membuat function sendiri karna function ini akan dipanggil berulang kali.

    #function ini bertujuan untuk menggabungkan array yang terpisah dan concate
    #dengan tanda _
def judulBuku(jb):
    concate = ""
    for i in range(len(jb)):
        if i == len(jb)-1:
            concate += jb[i] 
        else:
            concate += jb[i] + "_"
    return concate

buku = []

stop1 = True
while stop1:
    print()
    print("===== system pengelolaan buku 2 =======")
    print()
    print("[1] tambah buku \n[2] hapus buku \n[3] ubah buku \n[4] daftar buku \n[5] exit")
    act = input("pilih 1,2,3,4,5 > ")


    #jika user menambah buku / isi array
    if act == "1":
        print("==== tambah buku ====")
        books = input("buku : ").split()
        
        #menambah array
        buku += judulBuku(books).split()
        print()
        
        stop = True
        while stop:
            tmbh = input("tambah buku lagi ? : [y/t] ")
            if tmbh == "y":
                books = input("buku : ").split()
                buku += judulBuku(books).split()
            elif tmbh == "t":
                print("-terimakasih ! \nsilahkan pilih menu lain !")
                stop = False
            else:
                print("-inputan tidak ada!")

                
    #jika user menghapus buku / isi array
    elif act == "2":
        if len(buku) == 0:
            print("daftar buku kosong \ntambah buku terlebih dahulu !")
        else:
            print("===== hapus buku =====")
            for i in range(len(buku)):
                print("%i. %s"%(i+1,buku[i]))
            print()
            hps = int(input("hapus buku no: "))
            if len(buku) < hps:
                print("nomor buku tidak ditemukan")
            else:
                #menghapus buku / array
                buku[hps-1:hps]=[]

                
    #jika user mengubah buku / array yang sudah ada 
    elif act == "3":
        if len(buku) == 0:
            print("daftar buku kosong \ntambah buku terlebih dahulu !")
        else:
            print("==== ubah judul buku ====")
            for i in range(len(buku)):
                print("%i. %s"%(i+1,buku[i]))
            print()
            ubh = int(input("ubah judul buku no: "))
            judulBaru = input("judul baru buku : ").split()

            if len(buku) < ubh:
                print("nomor buku tidak ditemukan")
            else:
                #mengubah buku / array
                buku[ubh-1:ubh]=[judulBuku(judulBaru)]
    #jika user melihat daftar buku / array
    elif act == "4":
        if len(buku) == 0:
            print("daftar buku kosong \ntambah buku terlebih dahulu !")
        else:
            print("==== daftar buku ====")
            for i in range(len(buku)):
                print("%i. %s"%(i+1,buku[i]))
            print()
    #jika user ingin keluar dari program dan menghentikan perulangan
    elif act == "5":
        print("=====================")
        print("----terimakasih !----")
        print("=====================")
        stop1 = False

    else:
        print("perintah tidak ditemukan!")
            
            





            
        
