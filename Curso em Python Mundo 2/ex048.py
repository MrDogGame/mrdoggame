t = 0
t2 = 0
for c in range(1,500):
    if c % 3 == 0 and c % c == 0 and c % 2 == 1:
        t = t + 1
        t2 = c + t2
print('a soma de todos os {} valores é {}'.format(t,t2))