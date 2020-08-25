m1 = []
m2 = []
m3 = []
m4 = []
par = 0
maior = 0
t1 = []
for n in range(0,9):
    num = int(input('Digite um valor: '))
    if n < 3:
        t1.append(num)
        m1.append(t1[:])
        t1.clear()
    elif n > 2 and n < 6:
        t1.append(num)
        m2.append(t1[:])
        t1.clear()
    else:
        t1.append(num)
        m3.append(t1[:])
        t1.clear()

for n in m1:
    m4.append(n[0])
for n in m2:
    m4.append(n[0])
for n in m3:
    m4.append(n[0])
for n in m4:
    if n % 2 == 0:
        par = n + par
print('-=-'*40)        
print(f'A soma de todos os valores pares foi {par}')
print('-=-'*40)
print(f'A soma dos valores da terceira coluna é {m1[2][0] + m2[2][0] + m3[2][0]}')
print('-=-'*40)
for n in m2:
    if n[0] > maior:
        maior = n[0]
print(f'O maior valor da segunda linha foi {maior}')