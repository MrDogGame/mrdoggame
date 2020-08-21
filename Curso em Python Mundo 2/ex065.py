choice = 'S'
count = 0
maior = 0
tot = 0
menor = 9999999999
while choice != 'N':
    num = int(input('Digite um número: '))
    tot = tot + num
    count += 1
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    
    
    choice = str(input('Voçê quer digitar um número? S/N: ')).strip().upper()[0]
media = tot / count
print('Voçê digitou {} números.'.format(count))
print('O maior valor foi {} o menor {} e a média foi de {}'.format(maior,menor,media))
    