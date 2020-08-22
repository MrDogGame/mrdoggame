male = 0
female = 0
maioridade = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        maioridade += 1
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite novamente [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        male += 1
    if sexo == 'F' and idade < 20:
        female += 1
    choice = ' '
    while choice not in 'SN':    
        choice = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if choice == 'N':
        print('Volte sempre!')
        break
print(f'{maioridade} pessoas tem mais de 18 anos\n{male} homens foram cadastrado\n{female} mulheres tem menos de 20 anos!')