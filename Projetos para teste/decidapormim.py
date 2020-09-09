from random import randint

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


#programa principal
resposta = ["Sim", "Não", "Talvez", "Por que não?", "Vá", "Não sei", "Pode ser", "Talvez sim", "Talvez não", "Tenha Fé"]

while True:
    aleatorio = randint(0, 9)
    escolha = leialetra()
    if escolha == 'S':
        pergunta = facapergunta()
        if pergunta == 'L':
            print(resposta[aleatorio])
    else:
        break

