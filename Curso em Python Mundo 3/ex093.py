dados = {}
pontos = []
dados['Nome'] = str(input('Digite o nome do jogador: '))
partida = int(input('Digite a quantidade de partidas que jogou: '))
tot = 0
for g in range(0,partida):
    gols = int(input('Digite a quantidade de gol: '))
    pontos.append(gols)
    tot = tot + gols
dados['Gols'] = pontos[:]    
dados['Total'] = tot
print('-=-'*40)
print(dados)
print('-=-'*40)
for k , v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*40)
print(f'O jogador {dados.get("Nome")} jogou {partida} partidas')
count = 1
for v in pontos:
    print(f'    => Na partida {count}, fez {v} gols')
    count += 1
print(f'O total de gols foi {dados.get("Total")}')