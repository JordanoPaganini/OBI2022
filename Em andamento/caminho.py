qtd = int(input())

valores = []
escuros = []

for _ in range(qtd):
    valores.append(int(input()))

for index, i in enumerate(valores):
    j = valores[index+1]
    if j + i < 1000:
        escuros.append((i, j))

i = valores[0]
j = valores[-1]
if j + i < 1000:
    escuros.append((i, j))

print(int(len(escuros)/2))