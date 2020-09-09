import Dados

while True:
    escolha = int(input('''
    ----------------------------
    1 - Cadastrar nova pessoa.
    2 - Ver pessoas cadastradas.
    3 - Sair do programa.
    ----------------------------
    '''))

    if escolha == 1:

        novonome = Dados.cadastroNome()
        novaidade = Dados.cadastroIdade()

        arquivo = open('CADASTRO', 'r')
        conteudo = arquivo.readlines()
        conteudo.append(novonome)
        conteudo.append(str(novaidade))

        arquivo = open('CADASTRO', 'w')
        arquivo.writelines(conteudo)

        arquivo.close()
    elif escolha == 2:

        arquivo = open('CADASTRO', 'r')
        lista = arquivo.read()
        print(lista)

        arquivo.close()
    elif escolha == 3:
        break
    else:
        print('ERRO, opção invalida.')