dados = []
mulher = []
name = []
year = []
pessoa = {}
totida = 0
while True:
    nome = str(input('Digite o nome: '))
    sexo = str(input('Digite o sexo M/F ')).strip().upper()[0]
    idade = int(input('Digite a idade: '))
    pessoa['Nome'] = nome
    pessoa['Sexo'] = sexo
    pessoa['Idade'] = idade
    dados.append(pessoa.copy())
    name.append(nome)
    year.append(idade)
    totida = totida + idade
    if sexo in 'Ff':
        mulher.append(nome)
    choice = str(input('Deseja continuar S/N ')).strip().upper()[0]
    if choice in 'Nn':
        break
print(f'O total de pessoas cadastradas são de {len(dados)}')
media = totida / len(dados)
print(f'A idade media do grupo de pessoas cadastradas é de {media:.2f}')
print('As mulheres cadastrada foram: ')
for m in mulher:
    print(m)
print('As pessoas com idade acima da media foram:')
for n,d in enumerate(dados):
    if dados[n]['Idade'] > media:
        print(dados[n]['Nome'])