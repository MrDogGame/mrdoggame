aluno = {}
name = str(input('Digite o nome do aluno: '))
media = float(input('Digite a media do aluno: '))
aluno['Nome'] = name
aluno['Media'] = media
if media >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k,v in aluno.items():
    print(f'{k} é igual a {v}')