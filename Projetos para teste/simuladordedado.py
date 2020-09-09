from random import randint
from time import sleep

def leialetra():
    '''
        =>Função para validar letras.
        parm=msg: Recebe dados to tipo string sendo Ss ou Nn.
        return: String de valor S.
    '''
    while True:
        try:
            msg = str(input('Deseja jogar o dado? [s/n] ')).upper()[0]
        except KeyboardInterrupt:
            print('O usuário desistiu de inserir um dado!')
            break
        except IndexError:
            print('ERRO, nada digitado!')
        else:
            if msg not in 'SsNn' or msg in ' ':
                print('ERRO, DADO INVALIDO!')
            else:
                if msg in 'Nn':
                    print('Volte sempre, Obrigado!')
                    break
                else:
                    return 'S'
                    break


def Dado():
    '''
        =>Função gera um número entre 1 e 6.
    '''
    print('O dado foi rolado...')
    sleep(0.5)
    cpu = randint(1, 6)
    print(f'O valor do dado foi {cpu}')



#programa principal
while True:
    retorno = leialetra()
    if retorno == 'S':
        Dado()
    else:
        break

