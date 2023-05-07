valores = {'A': [10, 14], 'J': [11, 15], 'Q': [12, 16], 'K': [13, 17]}

dominate = input()[1]

luana = []
for i in range(3):
    luana.append(input().split())

edu = []
for i in range(3):
    edu.append(input().split())

total_luana = 0
total_edu = 0

for i in luana:
    if i[0][1] == dominate:
        total_luana += valores[f'{i[0][0]}'][1]
    else:
        total_luana += valores[f'{i[0][0]}'][0]
    
for i in edu:
    if i[0][1] == dominate:
        total_edu += valores[f'{i[0][0]}'][1]
    else:
        total_edu += valores[f'{i[0][0]}'][0]

if total_luana > total_edu:
    print('Luana')
elif total_edu > total_luana:
    print('Edu')
else:
    print('empate')