import PySimpleGUI
from random import randint

def telaPython():
    # Layout
    layout = [
        [PySimpleGUI.Text('Dado')],
        [PySimpleGUI.Text(Dado(), key='dado')],
        [PySimpleGUI.Button('Rolar', key='Botao'), PySimpleGUI.Button('Fechar')]
    ]
    # Create Windows
    janela = PySimpleGUI.Window('Simulador de DADO!', layout)

    while True:
        event, values = janela.read()
        dados = layout[1]

        if event == 'Botao':
            print(dados)

        if event == PySimpleGUI.WIN_CLOSED or event == 'Fechar':
            break
    janela.close()


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
    cpu = randint(1, 6)
    return cpu



'''
#programa principal
while True:
    retorno = leialetra()
    if retorno == 'S':
        Dado()
    else:
        break
'''
tela = telaPython()