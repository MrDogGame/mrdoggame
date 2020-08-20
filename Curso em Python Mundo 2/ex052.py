num = int(input('Digite um valor: '))
count = 0
for c in range(1,(num+1)):   
    if num % 1 == 0 and num % c == 0:
        count = count + 1
if count == 2:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')
