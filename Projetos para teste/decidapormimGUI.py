from random import randint
import PySimpleGUI as sg

#funções
def leialetra():
    '''
        =>Função para validar letras.
        parm=msg: Recebe dados to tipo string sendo Ss ou Nn.
        return: String de valor S.
    '''
    while True:
        try:
            msg = str(input('Deseja fazer uma pergunta? [s/n] ')).upper()[0]
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

def facapergunta():
    msg = str(input('Faça sua pergunta: ')).upper().strip().replace(' ','')
    if msg.isnumeric():
        return 'N'
    else:
        return 'L'


def listaResp():
    lista = ["Sim", "Não", "Talvez", "Por que não?", "Vá", "Não sei", "Pode ser", "Talvez sim", "Talvez não", "Tenha Fé"]
    aleatorio = randint(0, 9)
    return lista[aleatorio]


class Tela():
    def __init__(self):
        layout = [
            [sg.Text('Faça sua pergunta.')],
            [sg.InputText('', size=(20, 0), key='decisao')],
            [sg.Text('Resposta!', key='resp')],
            [sg.Button('Confirmar', key='ok'), sg.Button('Fechar', key='fechar')]
        ]

        janela = sg.Window('Decida por mim.', layout)

        while True:
            self.botao, self.valor = janela.read()

            if self.botao == 'ok':
                janela['resp'].update(listaResp())
            if self.botao == sg.WIN_CLOSED or self.botao == 'fechar':
                break

        janela.close()


#programa principal
'''

while True:
    
    escolha = leialetra()
    if escolha == 'S':
        pergunta = facapergunta()
        if pergunta == 'L':
            print(resposta[aleatorio])
    else:
        break
'''
tela = Tela()