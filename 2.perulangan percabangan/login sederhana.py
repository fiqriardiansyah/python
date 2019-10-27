#perulangan percabangan

'''

made by : fiqri ardiansyah

ini adalah program login sederhana ,untuk user dan admin masing2 username dan
password sudah diset.maka program akan mengecek yang mana admin dan user dan
yang tidak ada .jika inputan salah maka program akan dilangi sebanyak 3 kali
masukan = username dan password
'''



#user
usernameUser = "fiqri"
passwordUser = "fiqri123"

#admin
usernameAdmin = "admin"
passwordAdmin = "admin123"

print("===== login user =====")
print()


stop = 4
while stop != 0:
    user = input("username : ")
    pas = input("password : ")
    
    if user == "fiqri":
        if pas == "fiqri123":
            print("selamat datang "+user)
            stop = 0
        else:
            print("!!! password salah")
            stop -=1
            print("percobaan tinggal "+str(stop) if stop != 0 else
                  "percobaan anda habis")
            
    elif user == "admin":
        if pas == "admin123":
            print("selamt datang "+user)
            stop = 0
        else:
            print("!!! password salah")
            stop -= 1
            print("percobaan tinggal "+str(stop) if stop != 0 else
                  "percobaan anda habis")
            
    else:
        print("!!! username salah")
        stop-=1
        print("percobaan tinggal "+str(stop) if stop != 0 else
              "percobaan anda habis")
        
    
