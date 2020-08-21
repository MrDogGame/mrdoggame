num = int(input('Digite um valor: '))
mul = 1
while num != 0:
    if num != 0:
        mul = num * mul
    num = num - 1
print('Fatorial desse número é {}'.format(mul))