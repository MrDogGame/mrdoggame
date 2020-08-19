n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
#verificando o menor
if n1 < n2 and n3:
    print('O número {} é o menor!'.format(n1))
elif n2 < n3 and n1:
    print('O número {} é o menor!'.format(n2))
elif n3 < n2 and n1:
    print('O número {} é o menor!'.format(n3))
#verificando o maior
if n1 > n2 and n3:
    print('O número {} é o maior!'.format(n1))
elif n2 > n3 and n1:
    print('O número {} é o maior!'.format(n2))
elif n3 > n2 and n1:
    print('O número {} é o maior!'.format(n3))