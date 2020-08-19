casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do salário: '))
ano = int(input('Digite a quantidade de anos: '))

valorcasa = casa / (ano * 12)
valorsala = (salario*30)/100

if valorcasa <= valorsala:
    print('A casa será R${:.2f} por mês, você pode pegar o emprestimo!'.format(valorcasa))
else:
    print('A o valor da casa de R${:.2f} ultrapassa 30% do seu salário que é R${:.2f}'.format(valorcasa,valorsala))