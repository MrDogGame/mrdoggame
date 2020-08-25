total = []
nome = []
notas = []
lc = []
count = 0
while True:
    name = str(input('Digite o nome do aluno/a: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    nome.append(name)
    notas.append(n1)
    notas.append(n2)
    total.append(nome[:])
    total.append(notas[:])
    lc.append(total[:])
    nome.clear()
    notas.clear()
    total.clear()    
    choice = str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if choice in 'Nn':
        break
for n in lc:
    media = (n[1][0] + n[1][1]) / 2
    print(f'O aluno N{count}° de nome {n[0]} teve media {media}')
    count += 1
print(count)
while True:
    choice = int(input('Digite o numero do aluno ou 999 para sair: '))
    if choice == 999:
        break
    elif choice > count-1:
       print('Aluno não cadastrado!')
    else:
        print(f'Nota do aluno foi {lc[choice][1]}')    