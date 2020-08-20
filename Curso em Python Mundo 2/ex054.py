from datetime import date
dt = date.today().year
nm = 0
em = 0
for c in range(0,7):
    nasc = int(input('Digite o ano de nascimento: '))
    idade = dt - nasc
    if idade >= 21:
        em = em + 1
    else:
        nm = nm + 1
print('{} pessoas são de maior idade é {} pessoas ainda não são'.format(em,nm))
