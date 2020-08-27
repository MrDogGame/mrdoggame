from datetime import date
name = str(input('Digite o nome: '))
ano = int(input('Digite o ano de nascimento: '))
ctps = int(input('Digite o número da carteira de trabalho: '))
idade = date.today().year - ano
dados = {'Nome':name, 'Idade':idade, 'CTPS':ctps}
if ctps != 0:
    ancon = int(input('Digite o ano de contratação: '))
    salario = float(input('Digite o sálario: '))
    apo = (ancon + 35) - ano
    dados['Contratação'] = ancon
    dados['Salario'] = salario
    dados['Aposentadoria'] = apo
for k,v in dados.items():
    print(f'{k} tem o valor {v}')