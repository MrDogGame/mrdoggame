def dobro(num):
    """
        =>Função para calcular o drobro.
        parm=num: Recebe um número.
        return: Valor total.
    """
    r = num * 2
    return r


def metade(num):
    """
        =>Função para calcular a metade.
        parm=num: Recebe um número.
        return: Valor total.
    """
    r = num / 2
    return r


def aumento(num,taxa):
    """
        =>Função para calcular X% a mais de um número.
        parm=num: Recebe um número.
        parm=taxa: Recebe um número para a porcentagem.
        return: Valor total já com os X%.
    """
    r = num + ((num*taxa)/100)
    return r


def diminuir(num,taxa):
    """
        =>Função para calcular X% a menos de um número.
        parm=num: Recebe um número.
        parm=taxa: Recebe um número para a porcentagem.
        return: Valor total já com menos X% retirado.
    """
    r = num - ((num*taxa)/100)
    return r

