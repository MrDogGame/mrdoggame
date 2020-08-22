from random import randint
from time import sleep
jogada = ''
count = 0
while True:
    num = int(input('Digite um valor: '))
    mao = str(input('PAR ou ÍMPAR?: ')).strip().upper()
    print('-'*20)
    print('OPONENTE ESTA PENSANDO...')
    print('-'*20)
    sleep(1)
    cpu = random.randint(1,10)
    soma = cpu + num
    tot = soma % 2
    if  tot == 0:
        jogada = 'PAR'
    else:
        jogada = 'IMPAR'
    if mao == jogada:
        print('-='*20)
        print('Voçê ganhou!')
        print('=-'*20)
        count += 1
    else:
        print('~'*20)
        print('Voçê perdeu!')
        print('~'*20)
        break
print(f'Voçê ganhou {count} rodadas!')