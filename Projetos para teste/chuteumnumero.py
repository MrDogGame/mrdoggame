from random import randint

#funções
def generetor():
    '''
        =>Função para gerar um número aleatório.
        return: valor do número.
    '''
    aleatorio = randint(1,20)
    return aleatorio


def leianumero():
    '''
        =>Função para aceitar somente números inteiros.
        return: Valor inteiro.
    '''
    while True:
        try:
            num = int(input('Digite um valor inteiro: '))
        except KeyboardInterrupt:
            num = 0
            print('O usuário desistiu de inserir um número!')
            break
        except IndexError:
            num = 0
            print('ERROR, nada digitado.')
        except:
            print('ERROR, valor invalido.')
        else:
            return num
            break


#programa principal
numero_aleatorio = generetor()
print('Pensei em um número entra 1 e 20 tente adivinhar...')

while True:
    tentativa = leianumero()
    if tentativa < numero_aleatorio:
        print('O número que eu pensei é maior.')
    elif tentativa > numero_aleatorio:
        print('O número que eu pensei é menor.')
    else:
        print('Parabéns você acertou o número!')
        break