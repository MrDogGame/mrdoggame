

def leialetra():
    '''
        =>Função para validar letras.
        parm=msg: Recebe dados to tipo string sendo Ss ou Nn.
        return: String de valor S.
    '''
    while True:
        try:
            msg = str(input('Deseja jogar essa aventura? [s/n] ')).upper()[0]
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


def resposta():
    '''
        =>Função para validar letras.
        parm=msg: Recebe dados to tipo string.
        return: String.
    '''
    while True:
        try:
            msg = str(input('Qual sua resposta? ')).upper()[0]
        except KeyboardInterrupt:
            print('O usuário desistiu de inserir um dado!')
            break
        except IndexError:
            print('ERRO, nada digitado!')
        else:
            if msg not in 'EeDd' or msg in ' ':
                print('ERRO, DADO INVALIDO!')
            else:
                if msg in 'Dd':
                    return 'D'
                    break
                else:
                    return 'E'
                    break



#projeto principal
print('\033[34mGuie nosso personagem para a cidade!\033[m')
res_simples = leialetra()

if res_simples == 'S':
    print('Você esta caminhando e chega em uma bifurcação para onde irá esquerda ou direita?[E/D] ')
    res_esqdir = resposta()

    if res_esqdir == 'E':
        print('\033[31mVocê chegou em um riacho, após tentar atravesar você acabou se afogando por um deslise, que pena!\033[m')
    else:
        print('Você chegou em uma bifurcação com bandidos vá para esquerda ou para direita?[E/D]')
        res_esqdir = resposta()

        if res_esqdir == 'D':
            print('\033[31mVocê tentou enfrentar os bandidos mais foi massacrado por eles, que pena!\033[m')
        else:
            print('Você chegou a um desfiladeiro, irá pela esquerda ou direita?[E/D]')
            res_esqdir = resposta()

            if res_esqdir == 'D':
                print('\033[31mVocê tentou dar a volta pelo desfiladeiro mas caiu nele, que pena!\033[m')
            else:
                print('Você foi por outro caminho, chegando perto da cidade.')
                print('Existe uma rocha em seu caminho por qual lado deseja atravesar?[E/D] ')
                res_esqdir = resposta()

                if res_esqdir == 'E':
                    print('\033[31mA rocha rolou em cima de você, que pena!\033[m')
                else:
                    print('\033[32mParabéns você chegou a cidade, aproveite sua estadia.\033[m')