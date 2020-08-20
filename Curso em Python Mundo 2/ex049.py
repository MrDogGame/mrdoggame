num = int(input('Digite um número para ver sua tabuada: '))
count = 0
print('-='*20)
for c in range(0,11):
    print('{} x {:2} = {}'.format(num,count,num * count))
    count = count + 1
print('=-'*20)