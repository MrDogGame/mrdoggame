from random import randint
from time import sleep
num = int(input('Digite a quantidade de sorteios: '))
count = 1
print('------------------------')
print('''
    JOGO DA LOTO FACIL
''')
print('------------------------')
print('-=-'*40)
for l in range(0,num):
    l = []
    for n in range(0,6):
        cpu = randint(1,60)
        l.append(cpu)
    l.sort()
    print(f'Jogo {count}° {l}')
    count += 1
    sleep(1)
print('-=-'*40)