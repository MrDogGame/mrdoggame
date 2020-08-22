while True:    
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        print('Tabuada encerada!')
        break
    for c in range(1,11):
        mult = num * c
        print(f'{num:3} X {c:2} = {mult}') 