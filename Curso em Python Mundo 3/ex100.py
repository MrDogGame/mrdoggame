from random import randint
from time import sleep
num = []
def sorteia():
    print('Sorteando números')
    for n in range(0,5):
        cpu = randint(1,10)
        num.append(cpu)
        print(cpu,end=' ',flush=True)
        sleep(0.3)
        
def somapar(*n):
    sorteia()
    print()
    print('Somando todos os pares: ')
    par = 0
    for v in num:
        if v % 2 == 0:
            par = par + v
    print(par)       

somapar()