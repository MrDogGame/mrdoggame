main = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    main.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    choice = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if choice in 'N':
        break
print(f'Os valores digitados foram {main}')
print(f'Os valores pares digitado foram {par}')
print(f'Os valores impares digitado foram {impar}')