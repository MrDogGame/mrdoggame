print('''
-------------------------------------------
-       Caixa eletronico do santander     -
-------------------------------------------
''')
cedula50 = 50
cedula20 = 20
cedula10 = 10
cedula01 = 1
c50 = 0
c20 = 0
c10 = 0
c01 = 0
print('-='*40)
sac = int(input('Digite o valor a ser sacado:R$ '))
print('=-'*40)
tot = sac
while True:
    if cedula50 <= tot:
        tot = tot - 50
        c50 += 1 
    else:
        if cedula20 <= tot:
            tot = tot - 20
            c20 += 1
        else:
            if cedula10 <= tot:
                tot = tot - 10
                c10 += 1
            else:
                if cedula01 <= tot:
                    tot = tot - 1
                    c01 += 1
                else:
                    break
print(f'Foram impresso {c50} cedulas de R$50,00')
print(f'Foram impresso {c20} cedulas de R$20,00')
print(f'Foram impresso {c10} cedulas de R$10,00')
print(f'Foram impresso {c01} cedulas de R$1,00')