qtd = int(input())
valores = [str(x) for x in input().split()]

score = 0

def juntar_pares(tamanho_pares: int, lista: list = valores) -> list:
  nova_lista = []
  for i in range(0, len(lista), tamanho_pares):
      novo_par = ''.join(map(str, lista[i:i+tamanho_pares]))
      nova_lista.append(novo_par)
  return nova_lista

def juntar_pares_diferentes(args, lista_nova: list = valores.copy()):
  nova_lista = []
  score = 0
  for i in args:
    if score != 0:
        if len(lista_nova) == 0:
            return nova_lista
    novo_par = ''.join(lista_nova[0:i])
    nova_lista.append(novo_par)
    if i > len(lista_nova):
        for j in range(0, len(lista_nova)):
            lista_nova.pop(0)
    else:
        for j in range(0, i):
            lista_nova.pop(0)
    score += 1
    return nova_lista

def verificar(lista: list) -> bool:
    for i in range(len(lista) - 1):
        if lista[i] > lista[i+1]:
            return False
    return True

for i in range(1, len(valores)):
    lista = juntar_pares(tamanho_pares= i)
    if verificar(lista):
        score = 1
        print(lista[0])
        break

if score == 0:
    n = len(valores)
    args_possiveis = [range(1, n+1)] * n
    import itertools
    for args in itertools.product(*args_possiveis):
        pares = juntar_pares_diferentes(args).copy()
        if verificar(pares):
            print(pares[0])
            break