n_s, l_o = [int(x) for x in input().split()]
cidades, autonomia = [int(i) for i in input().split()]

dic_posicoes = {}

for j in range(1, cidades+1):
    dic_posicoes[f'{j}'] = input().split()

cidades_possiveis = {}

for i in dic_posicoes:

    cidades_perto = []
    for j in dic_posicoes:
        if i != j:
            valor = abs(int(dic_posicoes[f'{i}'][0]) - int(dic_posicoes[f'{j}'][0]))
            valor += abs(int(dic_posicoes[f'{i}'][1]) - int(dic_posicoes[f'{j}'][1]))
            distancia = valor * 50
            if distancia <= autonomia:
                cidades_perto.append(j)
    cidades_possiveis[str(i)] = cidades_perto

