num = int(input('Digite um número inteiro: '))
choice = int(input('Digite 1 para converter para binário, 2 para octal e 3 para hexadecimal: '))

if choice == 1:
    print('O número digitado convertido para binario é {}'.format(bin(num)[2:]))
elif choice == 2:
    print('O número digitado convertido para octal é {}'.format(oct(num)[2:]))
elif choice == 3:
    print('O número digitado convertido para hexadecimal é {}'.format(hex(num)[2:]))
else:
    print('Você digitou uma escolha inválida!')