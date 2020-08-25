m1 = []
m2 = []
m3 = []
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
print(f'''
{m1}
{m2}
{m3}
''')