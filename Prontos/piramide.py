dimensão = int(input())

plano = [[0 for i in range(8)]for i in range(dimensão)]

def camada(k, dimensão:int = dimensão):
    for i in range(k-1, dimensão-k+1):
        plano[k-1][i] = k

    for i in range(k-1, dimensão-k+1):
        plano[dimensão-k][i] = k        

    for j in range(k-1, dimensão-k+1):
        plano[j][k-1] = k        

    for j in range(k-1, dimensão-k+1):
        plano[j][dimensão-k] = k 

for i in range(1,2+dimensão//2):
    camada(i,dimensão)
    
for i in range(dimensão):
    for j in range(dimensão-1):
        print(plano[i][j], end=' ') 
    print(plano[i][dimensão-1])