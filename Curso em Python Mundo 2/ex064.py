count = 0
num = 0
while num != 999:
    num = int(input('Digite um  número [999] para parar: '))
    if num != 999:
        tot = num + num
        count += 1
print('A quantidade de números digitados foi {} e a soma deles é de {}'.format(count,tot))
