prim = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
count = 0
while count < 10:
    dec = prim + (count + 1) * raz
    print(dec,end=' -> ')
    count += 1
    