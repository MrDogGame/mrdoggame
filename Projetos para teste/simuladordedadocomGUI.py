import PySimpleGUI
from random import randint

class tela():
    def __init__(self):
        layout = [
            [PySimpleGUI.Text('Dado',size=(5,0)), PySimpleGUI.Text(Dado(),size=(5,0), key='dado')],
            [PySimpleGUI.Button('Rolar', key='Botao'), PySimpleGUI.Button('Fechar')]
        ]

        janela = PySimpleGUI.Window('Simulador de DADO.', layout)

        while True:
            self.event, self.values = janela.read()

            if self.event == 'Botao':
                janela['dado'].update(Dado())
            if self.event == PySimpleGUI.WIN_CLOSED or self.event == 'Fechar':
                break
        janela.close()


def Dado():
    '''
        =>Função gera um número entre 1 e 6.
    '''
    cpu = randint(1, 6)
    return cpu


tela = tela()