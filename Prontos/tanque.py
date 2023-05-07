consumo = int(input())
distancia = int(input())
qtd_tanque = int(input())

if (distancia/consumo)-qtd_tanque < 0:
    print('0.0')
else:
    print(f'{(distancia/consumo)-qtd_tanque:.1f}')