arm = 0
arn = 999999999999
for pess in range(1,6):
    peso = float(input('Digite o peso da pessoa: '))
    if peso > arm:
        arm = peso
    elif peso < arn:
        arn = peso
print('O maior peso foi {:.2f} é o menor foi {:.2f}!'.format(arm,arn))