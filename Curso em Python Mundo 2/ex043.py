peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
IMC = peso / (altura ** 2)

print('Seu IMC é de {:.2f}'.format(IMC))

if IMC < 18.5:
    print('Você esta abaixo do peso!')
elif 18.5 <= IMC < 25:
    print('Você esta no peso ideal!')
elif IMC == 25 or IMC < 30:
    print('Você esta sobrepeso')
elif IMC == 30 or IMC < 40:
    print('Você esta obeso!')
else:
    print('Vocẽ esta com obesidade mórbida!')