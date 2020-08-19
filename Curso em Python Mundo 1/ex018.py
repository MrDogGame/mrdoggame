import math
angulo = int(input('Digite o valor de um angulo: '))
seno = math.sin(math.radians(angulo))
conse = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O valor de seno é {:.2f} \nConseno é {:.2f} \nTangente é {:.2f}'.format(seno,conse,tang))