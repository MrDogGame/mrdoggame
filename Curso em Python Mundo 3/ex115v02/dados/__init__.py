def leiaInt():
    while True:
        try:
            num = int(input('Digite uma valor: '))
        except KeyboardInterrupt:
            num = 0
            print('Usuario desistiu de inserir um valor!')
            break
        except:
            print(f'ERROR: Digite um número inteiro válido!')
        else:
            return num
            break


def checarArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na hora de criar arquivo.')
    else:
        print('Arquivo foi criado.')


def cadastroCliente(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Ouve um ERRO no cadastro do cliente.')
    else:
        try:
            a.write(f'{nome:<30}{idade:^4}\n')
        except:
            print('ERRO ao inserir cadastro.')
        else:
            print('Cliente cadastrado com sucesso.')
    finally:
        a.close()


def lendoCliente(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO na leitura do arquivo.')
    else:
        print(a.read())
    finally:
        a.close()