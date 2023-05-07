qtd_dias = int(input())
soma_chuva = int(input())
chuva = [int(j) for j in input().split()]

qtd = 0
soma = 0
resp = 0

somas = [0 for x in range(10**6)]
somas[0] = 1

for i in chuva:
    soma += i
    if soma - soma_chuva >= 0:
        resp += somas[soma - soma_chuva]
    somas[soma] += 1

print(resp)