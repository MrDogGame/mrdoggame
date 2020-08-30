def minih():
    """
        =>Função para ver o manual de cada comando.
    """
    while True:
        msg = str(input('Digite um comando: ')).strip().lower()
        tot = len(f'Acessando o manual do comando {msg}')
        if msg == 'fim':
            break
        else:
            print('\033[41m~\033[m'*tot)
            print(f'\033[41mAcessando o manual do comando {msg}\033[m')
            print('\033[41m~\033[m'*tot)

            print(f'\033[42m{msg.__doc__}\033[m')

#programa principal
minih()