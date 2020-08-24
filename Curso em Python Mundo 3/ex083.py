expre = input('Digite uma expressão: ')
lista = []
lista2 = []
pd = ")"
pe = "("
count = 0
for c in expre:
    print(count)
    if c == pe:
        lista.append(c)   
    if count % 2 == 1:
        if c == pd:
            lista2.append(c)
            print('adicionou pd')
    if c in "()":
        count += 1      
if len(lista) == len(lista2):
    print('Expressão esta certa!')
else:
    print('Expressão esta errada!')           