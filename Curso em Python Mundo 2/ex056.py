countm = 0
bag = 0
bagidade = 0
male = ''
for pess in range(1,5):    
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite uma idade: '))
    sexo = int(input('Digite o sexo sendo 1 para masculino ou 2 para feminino: '))
    tot = bag + idade
    bag = tot
    if idade > bagidade:
        bagidade = idade
        male = nome
    if sexo == 2 and idade < 20:
        countm = countm + 1
media = bag / 4
print('-='*20)
print('O nome do homem mais velho é {}'.format(male))
print('A media de idade do grupo é de {:.0f} anos'.format(media))
print('A quantidade de mulheres é de {}'.format(countm))
print('=-'*20)