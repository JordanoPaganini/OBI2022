lado1 = int(input())
lado2 = int(input())
raio = int(input())
graus = int(input())

area_caixa = lado1 * lado2
area_pizza = 3.1415 * (raio ** 2)
pedacos = 360 % graus

if area_caixa >= area_pizza and pedacos == 0:
    print('S')
else:
    print('N')
