data = []
temp = []
gordo = []
magro = []
ideal = []
#cadastramento dos nomes e peso
while True:
    name = str(input('Digite o nome: '))
    weight = float(input('Digite o peso: '))
    temp.append(name)
    temp.append(weight)
    data.append(temp[:])
    temp.clear()
    choice=str(input('Deseja continuar S/N: ')).strip().upper()[0]
    if choice in 'Nn':
        break
print('-=-'*40)
print(f'O total de pessoas cadastradas foram {len(data)}')
print('-=-'*40)
#separação em lista das pessoas pesadas e leves
for p in data:
    if p[1] >= 100:
        gordo.append(p[0])
    elif p[1] <= 70:
        magro.append(p[0])
    else:
        ideal.append(p[0])
print('-=-'*40)
print(f'As pessoas acima do peso são {gordo}')
print('-=-'*40)
print(f'As pessoas abaixo do peso são {magro}')
print('-=-'*40)