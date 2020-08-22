totg = tot = 0
totp = 99999999
totn = ' '
while True:    
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço do produto: '))
    totg += preco
    if preco > 1000:
        tot += 1
    if preco < totp:
        totn = nome 
    choice = ' '
    while choice not in 'SN':
        choice = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if choice == 'N':
        print('Obrigado/a volte sempre!')
        break
print(f'O total gasto é de R${totg:.2f}')
print(f'O número de produtos acima de R$1000.00 é de {tot}')
print(f'O produto mais barato foi {totn}')