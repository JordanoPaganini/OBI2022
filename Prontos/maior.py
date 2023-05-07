menor = int(input())
maior = int(input())
total = int(input())

valores = {}

for i in range(menor, maior+1):
    numero = i
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero = numero // 10
    valores[soma] = i

try:
    valor = max([(valores[total])])
    print(valor)
except:
    print('-1')