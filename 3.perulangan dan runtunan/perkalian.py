#perulangan
'''

made by : fiqri ardiansyah


program ini akan memunculkan table perkalian

    -table : untuk menentukan banyak table perkalian
    -maximalPerkalian : untuk menentukan sampai perkalian berapa
'''


table = 10
maximalPerkalian = 10

for i in range(1,table+1):
    for j in range(1,maximalPerkalian+1):
        print("%d x %d = %d \n"%(i,j,i*j))
    print()
