print('-='*40)
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))
v3 = int(input('Digite mais um valor: '))
v4 = int(input('Digite e outro valor: '))
print('-='*40)
lista = (v1,v2,v3,v4)
print(f'O nove apareceu {lista.count(9)} veze/s')
print('-='*40)
if 3 in lista:
    print(f'O número trez apareceu pela primeira vez na {lista.index(3)+1}ª')
else:
    print('O valor 3 não foi digitado')
print('-='*40)
print(f'Os números pares foram',end='')
for c in lista:
    if c % 2 == 0:
        print(f' {c}',end='')
print('\n','-='*40)
