from datetime import date
dt = date.today().year
idade = int(input('Digite o ano de nascimento: '))
atual = dt - idade
print('Nascido no ano {} sua idade é {}'.format(idade,atual))
if atual <= 9:
    print('Você esta na categoria MIRIN!')
elif atual >= 10 and atual <= 14:
    print('Você esta na categoria INFANTIL!')
elif atual == 19:
    print('Você esta na categoria JUNIOR!')
elif atual == 20:
    print('Você esta na categoria SÊNIOR!')
else:
    print('Você esta na categoria MASTER!')

