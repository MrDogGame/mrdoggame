def linha(tam):
    print('-'*tam)


def laybel(msg='Menu vazio'):
    linha(40)
    print(f'{msg:^30}')
    linha(40)


def opcao(opg):
    print(f'{opg:<30}')

def layout():
    laybel('Menu de cadastro')
    opcao('1 - Cadastro de cliente.')
    opcao('2 - Ver clientes cadastrados.')
    opcao('3 - Sair do programa.')
    linha(40)