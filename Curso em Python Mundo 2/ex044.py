preco = float(input('Digite o valor do produto:R$ '))
print('1 = A vista dinheiro ou cheque! com 10% de desconto. \n2 = A vista no cartão! com 5% de desconto. \n3 = 2x no cartão! preço normal. \n4 = 3x ou mais no cartão! 20% de juros.')
choice = int(input('Digite a forma de pagamento de 1 a 4: '))

if choice == 1:
    t = preco - (preco * 10 / 100)
    print('O valor a pagar sera de R${:.2f}'.format(t))
elif choice == 2:
    t = preco - (preco * 5 / 100)
    print('O valor a pagar sera de R${:.2f}'.format(t))
elif choice == 3:
    print('O valor a pagar sera de R${:.2f}'.format(preco))
elif choice == 4:
    t = preco + (preco * 20 / 100)
    print('O valor a pagar sera de R${:.2f}'.format(t))
else:
    print('Opção invalida!')