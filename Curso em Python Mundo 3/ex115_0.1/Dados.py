def cadastroNome():
    while True:
        try:
            cad = str(input('Digite um nome para cadastra-lo: ')).strip()
        except KeyboardInterrupt:
            print('Usuário desistiu de inserir um dado!')
            break
        else:
            if cad.isnumeric():
                print('ERROR')
            else:
                return cad.ljust(20)
                break


def cadastroIdade():
    while True:
        try:
            num = int(input('Digite a idade: '))
        except KeyboardInterrupt:
            num = 0
            print('Usuário desistiu de inserir um dado!')
            break
        except:
            print('ERRO, dado invalido!')
        else:
            return f'{num}\n'
            break