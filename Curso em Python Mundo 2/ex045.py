import random
print('''
[1] = Pedra!
[2] = Papel!
[3] = Tesoura!
''')
choice = int(input('Qual será a sua jogada!: '))
cpu = random.randint(1,3)
cpujog = ''
if cpu == 1:
    cpujog = 'Pedra!'
elif cpu == 2:
    cpujog = 'Papel!'
elif cpu == 3:
    cpujog = 'Tesoura!'
print('-='*20)
print('O computador escolheu {}'.format(cpujog))
print('-='*20)
if choice == 1 and cpu == 1:
    print('Você empatou!')
elif choice == 2 and cpu == 2:
    print('Você empatou!')
elif choice == 3 and cpu == 3:
    print('Você empatou!')
elif choice == 1 and cpu == 3:
    print('Você ganhou!')
elif choice == 2 and cpu == 1:
    print('Você ganhou!')
elif choice == 3 and cpu == 2:
    print('Você ganhou!')
elif choice >= 4:
    print('Você escolheu a opção errada!')
else:
    print('Você perdeu!')
