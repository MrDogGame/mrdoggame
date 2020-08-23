num = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
'quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

teclado = int(input('Digite um número de 0 a 20: '))

if teclado < 0 or teclado > 20:
    teclado = int(input('tente novamente, digite um número de 0 a 20: '))

print(num[teclado])