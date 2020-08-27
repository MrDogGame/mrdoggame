time = []
jogador = {}
gols = []
tot = 0
while True:
    #entrada de dados
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Digite a quantidade de partidas: '))
    #for para calcular a quantidade de gols de cada partida
    for g in range(0,partidas):
        pontos = int(input('Digite a quantidade de gol: '))
        gols.append(pontos)
        tot += pontos
    #adicionando gols e o total de gols somado no time
    jogador['Gols'] = gols[:]
    gols.clear()
    jogador['Total'] = tot
    tot = 0
    #adicionando jogador em times
    time.append(jogador.copy())
    #escolha par sair ou continuar no programa
    choice = str(input('Deseja continuar S/N ')).strip().upper()[0]
    if choice in 'SN':
        if choice in 'Nn':
            break
    else:
        print('ERROR!')        
#mostra a lista de jogadores
print('-=-'*40)
print('Cod  Nome    Gols    Total')
for n , d in enumerate(time):
    print(f'{n}  {d["Nome"]}    {d["Gols"]}     {d["Total"]}')
print('-=-'*40)
#levantamento do jogador
tott = len(time)
print(tott)
while True:
    part = int(input('Qual jogador deseja ver(999 para sair): '))
    if part == 999:
            break
    else:
        if part <= tott - 1:    
            for n , g in enumerate(time[part]['Gols']):
                print(f'Na partida {n+1} fez {g} gols.')
        else:
            print('Jogador não existe')