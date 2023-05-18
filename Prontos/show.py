amigas, n_filas, n_assentos = [int(x) for x in input().split()]

mapa = {}
possiveis = [-1]
score = 0

for i in range(n_filas, 0, -1):
    mapa[i] =  [int(j) for j in input().split()]

for i in range(1, len(mapa)+1):
    fileira = mapa[i]
    if n_assentos - amigas >= sum(fileira):
        for j in mapa[i]:
            if j == 0: 
                score += 1
            else: score = 0
        if score >= amigas:
            possiveis.append(i)
            
print(min(possiveis))
