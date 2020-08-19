frase = str(input('Digite uma frase: ')).strip()
u = frase.upper()
c = u.count('A')
f = u.find('A')+1
fr = u.rfind('A')+1
print('A letra A aparece {} vezes.'.format(c))
print('A letra primeira A aparece na posição {}.'.format(f))
print('A letra ultima A aparece na posição {}.'.format(fr))
