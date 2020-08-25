data = []
par = []
impar = []
for p in range(0,8):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
data.append(par[:])
data.append(impar[:])
print(f'Os números pares foram {sorted(data[0])}')
print(f'Os números impares foram {sorted(data[1])}')