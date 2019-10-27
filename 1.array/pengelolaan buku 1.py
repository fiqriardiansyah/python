#system pengelolaan buku 1
'''

made by : fiqri ardiansyah


program system pengelolaan buku 1 ini adalah program pengeloloaan array
sederhana yang mempunyai fitur menambahkan isi array,menghapus isi array
dan melihat isi array , user bisa memilih fitur tersebut dengan menginputkan
nomor yang terdaftar
'''

#rak buku
buku = ["harry potter","game of thron","the mummy"]

print("==== system pengelolaan buku 1 =====")
print()
print("daftar buku : ")

#tampilkan isi array
for i in range(len(buku)):
    print("%d. %s"%(i+1,buku[i]))
#program akan mengulang terus sampai user memilih untuk keluar
stop = True
while stop:
    print()
    print("pengelolaan buku : ")
    print("[1] tambah buku \n[2] lihat daftar buku \n[3] hapus buku \n[4] keluar")
    act = int(input("pilih 1,2,3,4 >"))

    if act == 1:
        tambah = input("judul buku : ").split()
        buku+=tambah
        print()
        print("-- daftar buku : ")
        for i in range(len(buku)):
            print("--- %d. %s"%(i+1,buku[i]))
    elif act == 2:
        print()
        print("-- daftar buku : ")
        for i in range(len(buku)):
            print("--- %d. %s"%(i+1,buku[i]))
    elif act == 3:
        print()
        print("-- daftar buku : ")
        for i in range(len(buku)):
            print("--- %d. %s"%(i+1,buku[i]))
        print("hapus buku")
        hapus = int(input("no buku :  "))
        buku[hapus-1:hapus]=[]
        print("-- daftar buku : ")
        for i in range(len(buku)):
            print("--- %d. %s"%(i+1,buku[i]))
    elif act == 4:
        stop = False
        print("Terimakasih!!")
    else:
        print("pilihan tidak ada")
