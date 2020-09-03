while True:
    try:
        num = int(input('Digite um número inteiro: '))
    except KeyboardInterrupt:
        num = 0
        print('Usuario desistiu de inserir um valor!')
        break
    except:
        print(f'ERROR: Digite um número inteiro válido!')
    else:
        print(f'O número digitado foi {num}.')
        break


while True:
    try:
        real = float(input('Digite um número real: '))
    except KeyboardInterrupt:
        real = 0
        print('Usuario desistiu de inserir um valor!')
        break
    except:
        print(f'ERROR: Digite um número real válido!')
    else:
        print(f'O número digitado foi {real}.')
        break