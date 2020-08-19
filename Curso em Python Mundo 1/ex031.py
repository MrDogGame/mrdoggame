vel = float(input('Digite a distância a ser percorrida: '))
if vel > 200.00:
    d1 = vel * 0.45
    print('O valor sera de R${:.2f}'.format(d1))
else:
    d2 = vel * 0.50
    print('O valor sera de R${:.2f}'.format(d2))
