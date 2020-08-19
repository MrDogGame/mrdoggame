idade = int(input('Digite o ano de seu nascimento: '))
anoat = int(input('Digite o ano atual: '))
idano = anoat - idade

if idano < 17:
    print('Você ainda vai se alistar!')
elif idano == 17 or idano == 18:
    print('Esta na hora de se alistar!')
else:
    print('Você passou da idade de se alistar!')