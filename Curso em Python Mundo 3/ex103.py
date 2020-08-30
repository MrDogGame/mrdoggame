def ficha(nome='Desconhecido',gols=0):
    """
        =>Mostra a ficha de um jogador.
        parm=nome: Nome do jogador, padrão desconhecido.
        parm=gols: Quantidade de gols, padrão 0.
        return: A ficha.
    """
    n = str(input('Digite o nome do jogador: '))
    g = str(input('Digite a quantidade de gols: '))
    if n.strip() == '':
        n = nome
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
     
    return f'O jogador {n} fez {g} gols.'

#Programa principal
print(ficha())