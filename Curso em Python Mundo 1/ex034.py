sal = float(input('Digite o salário: '))
if sal > 1250.00:
    a = sal * 0.10
    print('Salário de R${} ficou R${}!'.format(sal,a+sal))
else:
    b = sal * 0.15
    print('Salário de R${} ficou R${}!'.format(sal,b+sal))
