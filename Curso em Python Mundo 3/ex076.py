compras = (
    'Banana' , 2.00, 'Leite', 3.75, 'Peixe', 2.75, 'chá', 6.50, 'arroz', 10.50
)
print('''
------------------------------
        lista de compras
------------------------------
''')
for c in compras:
    if type(c) != float:
        print(f'{c:.<20}',end='')
    #print(end='.>20')
    if type(c) != str:
        print(f'R$: {c:.2f}')