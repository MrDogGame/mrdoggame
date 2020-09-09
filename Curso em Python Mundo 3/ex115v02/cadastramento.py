import menu
import dados

arq = 'CADASTRO.txt'

if dados.checarArquivo(arq):
    print('Arquivo existente.')
else:
    print('Arquivo não existe, sendo criado!')
    dados.criarArquivo(arq)

while True:
    menu.layout()
    opcao = dados.leiaInt()
    menu.linha(40)
    if opcao == 1:
        nome = str(input('Digite o nome: '))
        idade = dados.leiaInt()
        dados.cadastroCliente(arq, nome, idade)
    elif opcao == 2:
        print('Nome'.ljust(30), 'Idade')
        dados.lendoCliente(arq)
    elif opcao == 3:
        print('Saindo do programa')
        break
    else:
        print('\033[31mERRO, opção invalida.\033[m')
