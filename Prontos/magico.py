from collections import Counter

dimensão = int(input())

quadrado = {}
soma_linhas = {}

for i in range(1, dimensão+1):
    quadrado[i] = [int(x) for x in input().split()]

soma_colunas = [sum([quadrado[chave][indice] for chave in quadrado]) for indice in range(len(quadrado[1]))]

for i in range(1, dimensão+1):
    linha = quadrado[i]
    soma_linhas[i] = sum(linha)

counter_soma_linhas = Counter(list(soma_linhas.values()))
counter_soma_colunas = Counter(soma_colunas)

for i in counter_soma_linhas:
    if counter_soma_linhas[i] == 1:
        linha_erro = next(chave for chave, valor in soma_linhas.items() if valor == i)

for i in counter_soma_colunas:
    if counter_soma_linhas[i] == 1:
        coluna_erro = soma_colunas.index(i) + 1

print(max(counter_soma_linhas.keys())-min(counter_soma_linhas.keys()))
print(linha_erro)
print(coluna_erro)