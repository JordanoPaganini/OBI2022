colunas, linhas, cameras = [int(x) for x in input().split()]

plano = {}

for i in range(1, linhas+1):
    plano[i] = [0 for x in range(colunas)]

for _ in range(cameras):
    x, y, direction = input().split()
    plano[int(y)][int(x)-1] = 1
    if direction == 'O':
        j = int(x) - 1
        while j != -1:
            plano[int(y)][j] = 1
            j -= 1
    if direction == 'L':
        j = int(x)
        while j != colunas:
            plano[int(y)][j] = 1
            j += 1
    if direction == 'N':
        j = int(y) - 1
        while j != 0:
            plano[j][int(x)-1] = 1
            j -= 1
    if direction == 'S':
        j = int(y) + 1
        while j != linhas+1:
            plano[j][int(x)-1] = 1
            j += 1

for i in range(1, linhas+1):
        print(plano[i])