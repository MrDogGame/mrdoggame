lista = []
#cadastramento de numero na lista
while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    enc = lista.count(num)
    if enc > 1:
        print('Número já esta cadastrado!')
        lista.pop()
    print('-='*40)
    choice = str(input('Deseja continuar? S/N: ')).strip().upper()[0]
    print('=-'*40)
    if choice in 'N':
        break
print('--'*40)
print(f'Os valores digitado foi {sorted(lista)}')