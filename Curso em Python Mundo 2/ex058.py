import random
from time import sleep
player = 0
r = random.randint(0,10)
count = 0
print('''
Tente adivinhar o que número o computador pensou!!!
''')
while player != r:
    player = int(input('Digite um número: '))
    print('PROCESSANDO...')
    sleep(1)
    if player != r:
        print('Que pena você perdeu! =/')
        count = count + 1
    else:
        print('Parábens você ganhou! XD')
print('Foram necessarios {} jogadas para voçê ganhar!'.format(count))