def dobro(num=0):
    """
        =>Função para calcular o drobro.
        parm=num: Recebe um número.
        return: Valor total.
    """
    r = num * 2
    return r


def metade(num=0):
    """
        =>Função para calcular a metade.
        parm=num: Recebe um número.
        return: Valor total.
    """
    r = num / 2
    return r


def aumento(num=0,taxa=0):
    """
        =>Função para calcular X% a mais de um número.
        parm=num: Recebe um número.
        parm=taxa: Recebe um número para a porcentagem.
        return: Valor total já com os X%.
    """
    r = num + ((num*taxa)/100)
    return r


def diminuir(num=0,taxa=0):
    """
        =>Função para calcular X% a menos de um número.
        parm=num: Recebe um número.
        parm=taxa: Recebe um número para a porcentagem.
        return: Valor total já com menos X% retirado.
    """
    r = num - ((num*taxa)/100)
    return r


def moeda(num=0,sim='R$'):
    """
        =>Função para converter para moeda.
        parm=num: Recebe um número.
        parm=sim: Recebe um símbolo, por pradão é o real.
        return: Valor convertido.
    """
    return f'{sim}{num:>5.2f}'.replace('.',',')