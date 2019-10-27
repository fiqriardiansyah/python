#perulangan
'''
program ini akan menghasil segita bintang yang tidak akan pernah berhenti
(infinite loop)
'''


true = True
while true:
    for i in range(1,11):
        for j in range(1,i):
            print("*",end="")
        print()

    for i in range(11,1,-1):
        for j in range(i,1,-1):
            print("*",end="")
        print() 
