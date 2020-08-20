# Tive dificuldade por conta de conceitos mátematicos errados.
raz = int(input('Digite um valor para a razão: '))
pt = int(input('Digite o valor do primeiro termo: '))
dc = pt + (10 - 1) * raz
for c in range(pt,dc,raz):
    print(c)