#infelizmente fiquei travado na parte de ordernar a lista, esse exercicio eu fiz usando a resposta do video como base.
lista = []
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if len(lista) == 0 or num > max(lista):
        lista.append(num)
        print('Numero vai ser inserido no final')
    else: 
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                print('Numero vai ser inserido na {pos}°')
                lista.insert(pos,num)
                break 
            pos += 1
print(f'Os valores digitado foi {lista}')