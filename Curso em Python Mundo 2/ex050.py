count = 0
num = 0
for c in range(1,7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        count = num + count   
print('A soma de todos os números pares é {}'.format(count))