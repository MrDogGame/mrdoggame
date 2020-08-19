vel = float(input('Digite a velocidade do carro: '))
if vel > 80.00:
    m = (vel - 80) * 7
    print('Você foi multado em R${:.2f}'.format(m))
