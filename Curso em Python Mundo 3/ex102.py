def fatorial(num,show=False):
    """
        => Função para cálcular um fatorial.
        parm=num: Recebe o valor do fatorial sendo em reverso.
        parm=show: Padrão Oculto, mostra o passo a passo do fatorial.
        return: O valor o fatorial de um número num. 
    """
    f = 1
    for c in range(num,0,-1):
        f = f * c
        if show == True:
            print(f'{c}', end=' ')
    print()
    return f'O valor do fatorial {num} é {f}'

    
#Programa principal
print(fatorial(5,True))