prim = int(input('Digite o primeiro termo: '))
ult = int(input('Digite o ultimo termo: '))
raz = int(input('Digite a razão: '))
count = 0
while count < ult:
    dec = prim + (count + 1) * raz
    print(dec,end=' -> ')
    count += 1
    if count >= ult:
        print('FIM')
        print('\n')
        nova = int(input('Digite 0 para sair ou quantos termos quer mostrar: '))
        if nova != 0:
            prim = int(input('Digite o primeiro termo: '))
            ult = nova
            raz = int(input('Digite a razão: '))
            count = 0
