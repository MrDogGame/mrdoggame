frase = input('Digite um frase: ').upper()
frase = frase.replace(' ','')
total = len(frase)
v1 = ''
v2 = ''
for c in range(0,total):
    v1 = frase[c]
for b in range(total-1,-1,-1):
    v2 = frase[b]
if v1 == v2:
    print('Essa frase é PALÍNDROMO')
else:
    print('Essa frase não é PALÍNDROMO')