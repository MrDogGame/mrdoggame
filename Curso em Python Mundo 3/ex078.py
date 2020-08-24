lista = []
maiorn = 0
menorn = 0
#adiciono numeros na lista
for c in range(0,5):
    num = int(input("Digite um valor: "))
    lista.append(num)
    if c == 0:
        maiorn = menorn = num
    else:    
        if num > maiorn:
            maiorn = num
        if num < menorn:
            menorn = num
print('-='*40)
print(f'O maior número foi {maiorn}')
print(f'O menor número foi {menorn}')
print('=-'*40)
#contagem
for con,v in enumerate(lista):
    if v == maiorn:
        print(f'O valor {v} esta na posição {con}°')
    if v == menorn:
        print(f'O valor {v} esta na posição {con}°')
print('-'*40)