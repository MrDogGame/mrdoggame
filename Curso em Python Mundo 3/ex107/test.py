import moeda


n = float(input('Digite o valor a ser calculado R$'))
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Metade de R${n} é R${moeda.metade(n)}')
print(f'O aumento de R${n} em 10% é R${moeda.aumento(n,10)}')
print(f'O valor de R${n} com 13% a menos é R${moeda.diminuir(n,13)}')