from random import randint
ficha = {}
rank = {}
lista = []
count = 1
print('Os valores sorteados foram:')
for n in range(0,4):
    cpu = randint(1,6)
    ficha[n] = cpu
    print(f'O jogador{n} tirou {ficha[n]}')
for n in ficha.values():
    lista.append(n)
lista.sort()
print('O ranking dos jogadores foram:')
for n in lista:
    rank[f'Jogador{count}'] = n
    print(f'{count}° lugar: Jogador{count} com {rank[f"Jogador{count}"]} pontos')
    count += 1