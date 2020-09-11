from random import randint
from time import sleep
import PySimpleGUI as sg

#funções
def generetor():
    '''
        =>Função para gerar um número aleatório.
        return: valor do número.
    '''
    aleatorio = randint(1,20)
    return aleatorio


class tela():
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Pensei num número de 1 a 20!')],
            [sg.Input('',size=(5,0),key='jogada'), sg.Text('Adivinhe', key='dica')],
            [sg.Button('Comparar', key='botaook'), sg.Button('Fechar', key='fechar')]
        ]
        #janela
        janela = sg.Window('Chute um número', layout)

        while True:
            self.Botao, self.valor = janela.read()

            if self.Botao == 'botaook':
                if self.valor['jogada'] > str(num):
                    janela['dica'].update('Menor')
                elif self.valor['jogada'] < str(num):
                    janela['dica'].update('Maior')
                else:
                    janela['dica'].update('Acertou')

            if self.Botao == sg.WIN_CLOSED or self.Botao == 'fechar':
                break

        janela.close()


num = generetor()
print(num)
tela = tela()
