km = float(input('Digite a quantidade de Km andado: '))
d = int(input('Digite a quantidade de dias: '))
t = (km*0.15)+(d*60)
print('O total para pagar sera de R${:.2f}'.format(t))