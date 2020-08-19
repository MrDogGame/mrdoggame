nome = str(input('Digite seu nome completo: ')).strip()
p = nome.split()
print('Seu primeiro nome é {}.'.format(p[0]))
print('Seu ultimo nome é {}.'.format(p[len(p)-1]))
