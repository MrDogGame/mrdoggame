def leiaDinheiro():
    """
        =>Função para receber somente valor númerico,
        funciona como um input mas para números.
        return: O valor númerico.
    """
    while True:
        num = input('Digite um valor : R$').strip().replace(',','.')
        if num.isalpha() or num == '':
            print('ERRO, VALOR INVALIDO!')
        else:
            num = float(num)
            return num
            break