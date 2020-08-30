def notas(*n,sit=False):
    """
        =>Função para media de notas inseridas.
        parm=n: Recebe números flutuantes sem limite de quantidade.
        parm=sit: Padrão False, se verdadeiro mostra a media da turma.
        return: O dicionairo completo.
    """
    ficha = {}
    ficha['Notas'] = n
    ficha['Total'] = len(ficha['Notas'])
    ficha['Menor'] = min(ficha['Notas'])
    ficha['Maior'] = max(ficha['Notas'])
    c = 0
    for n in ficha['Notas']:
        c = c + n
    ficha['Media'] = c / ficha['Total']
    if sit == True:
        if ficha['Media'] > 7:
            ficha['Situação'] = 'BOA'
        elif ficha['Media'] < 4:
            ficha['Situação'] = 'RUIM'
        else:
            ficha['Situação'] = 'RAZOAVEL'
    return ficha

#Programa principal    
n = notas(6,4,1,sit=False)
print(n)