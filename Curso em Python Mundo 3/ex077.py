lista = ('COMPUTADOR','VIDEOGAME','CACHORRO','DINHEIRO','PROGRAMAR')
count = 0
for c in lista:
    print(lista[count])
    if 'A' in  lista[count]:
        print('A')
    if 'E' in  lista[count]:
        print('E')
    if 'I' in  lista[count]:
        print('I')
    if 'O' in  lista[count]:
        print('O')
    if 'U' in  lista[count]:
        print('U')    
    count += 1
    
'''
palavras = (um monte de palavras aki!)
for p in palavras:
    print('na palavras {p} temos tantas vogais')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra)
'''