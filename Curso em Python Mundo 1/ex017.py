from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hp = hypot(co,ca)
print('O valor da hipotenusa é {:.2f}.'.format(hp))