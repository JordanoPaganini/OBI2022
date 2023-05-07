total = 0

for _ in range(2):
    idade = int(input())
    if idade <= 17:
        total += 15
    elif idade <= 59:
        total += 30
    else: total += 20

print(total)