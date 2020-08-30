def voto(anon=0):
    """
        => Função para saber o estado eleitoral.
        parm=anon: recebe o ano de nascimento, se vazio recebe 0.
        return: O valor dentro de uma lista mostrando o estado do eleitor.
    """
    from datetime import date
    idade = date.today().year - anon
    parm = ['OBRIGATÓRIO','NEGADO','OPCIONAL']
    if idade >= 18 and idade <= 65:
        return parm[0]
    elif idade < 17:
        return parm[1]
    else:
        return parm[2]

#Programa principal    
year = int(input('Digite um ano de nascimento: '))
fun = voto(year)
print(f'Nascido em {year} seu voto é {fun}')