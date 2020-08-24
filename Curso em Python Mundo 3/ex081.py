lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    choice = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if choice in 'N':
        break
print(f'O total de números digitado foi de {len(lista)}.')
print(f'Os valores inverso foram {sorted(lista , reverse=True)}')
if 5 not in lista:
    print('O valor 5 não esta na lista.')
else:
    print('O valor 5 esta na lista.')