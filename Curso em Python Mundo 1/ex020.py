import random
a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')
sor = a1,a2,a3,a4
r = random.sample(sor,4)
print('O ordem do sorteio é {}'.format(r))