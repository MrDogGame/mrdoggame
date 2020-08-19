import random
num = int(input('Digite um número: '))
r = random.randint(0,5)
print('PROCESSANDO...')
if num == r:
    print('Você venceu!')
else:
    print('Você perdeu!')
print('====FIM====')