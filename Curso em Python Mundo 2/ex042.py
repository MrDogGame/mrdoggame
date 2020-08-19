r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')

    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Esse é um triângulo EQUILÁTERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse é um triângulo ISÓSCELES!')
    else:
        print('Essse é um triângulo ESCALENO!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')