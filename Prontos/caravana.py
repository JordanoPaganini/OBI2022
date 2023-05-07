qtd = int(input())

pesos = list()

for i in range(qtd): 
  pesos.append(int(input()))

peso_certo = sum(pesos) / qtd

for i in pesos:
  print(f'{peso_certo - i}')
