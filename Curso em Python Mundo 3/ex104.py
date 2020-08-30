def leiaint():
    """
        =>Função para leitura de númericos.
        return: Valor númerico digitado.
    """
    while True:
        num = input('Digite um valor: ')
        if num.isnumeric():
            break 
        else:
            print('ERROR, DADO INVALIDO!')
    return num


#Programa principal
n = leiaint()
print(f'O número digitado é {n}')