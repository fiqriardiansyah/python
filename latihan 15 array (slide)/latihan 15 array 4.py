print("==== jumlah angka prima didalam array =====")
print()

arr = input("angka : ").split()

prima = 0
tdk = 0





for i in range(len(arr)):
    if int(arr[i]) > 1:
        for s in range(2,int(arr[i]),1):
            if int(arr[i]) % s == 0:
                if int(arr[i]) ==  2:
                    prima += 1
                    
                break
            else:
                prima += 1
                break


print("banyaknya bilangan prima adalah : ",prima)
