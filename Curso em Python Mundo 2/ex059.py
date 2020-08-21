print('''
[1] = somar
[2] = mútiplicar
[3] = maior
[4] = novos números
[5] = Sair do programa 
''')
choice = 0
v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))
while choice != 5:
    choice = int(input('Digite qual opção: '))
    if choice == 1:
        s = v1 + v2
        print('A soma dos valores é {}'.format(s))
    elif choice == 2:
        m = v1 * v2
        print('A mútiplicação dos valores é {}'.format(m))
    elif choice == 3:
        if v1 > v2:
            print('O maior número é {}'.format(v1))
        elif v2 > v1:
            print('O maior número é {}'.format(v2))
        else:
            print('Os dois valores são iguais!')
    elif choice == 4:
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
    elif choice != 5:
        print('Opção invalida digite novamente!')