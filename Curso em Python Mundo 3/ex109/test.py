from ex109 import moeda


n = float(input('Digite o valor a ser calculado R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'Metade de {moeda.moeda(n)} é {moeda.metade(n)}')
print(f'O aumento de {moeda.moeda(n)} em 10% é {moeda.aumento(n,10)}')
print(f'O valor de {moeda.moeda(n)} com 13% a menos é {moeda.diminuir(n,13)}')