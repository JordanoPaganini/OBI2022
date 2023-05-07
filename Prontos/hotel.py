valor = int(input())
aumento = int(input())
dia_entrada = int(input())

diaria = 0
dias_hospedado = 32 - dia_entrada

if dia_entrada == 1:
    diaria = valor
elif dia_entrada <= 15:
    diaria = valor + (aumento * (dia_entrada - 1))
else:
     diaria = valor + (aumento * 14)

print(dias_hospedado * diaria)