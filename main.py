from operacoesbd import *

numero = int(input('Digite um número: '))

conexao = criarConexao('127.0.0.1', 'root', ':8k&7!/2uXJz', 'ouvidoria')
print('1 - Listar\n2 - Listar tipo de manifestação\n3 - Pesquisar\n4 - Inserir\n5 - Atualizar\n6 - Deletar\n7 - Sair')

while numero != 7:
    op = int(input('Digite a opção que deseja: '))

    if op == 1:
        listar = 'select * from manifestacoes'
        manifestacoes = listarBancoDados(conexao, listar)

        if len(manifestacoes) == 0:
            print('Não tem manifestações')
        else:
            print('Manifestsaçõ es encontradas')

            for i in manifestacoes:
                print('código', i[0], 'autor', i[1], 'categoria', i[2], 'descrição', i[3], 'data e hora', i[4])

    elif op == 2:
        pesquisar_categoria = input('Digite a categoria: ')
        listar_por_categoria = 'select * from manifestacoes where categoria = ' + pesquisar_categoria
        manifestacoes = listarBancoDados(conexao, listar_por_categoria)

        if len(manifestacoes) == 0:
            print('Não existe manifestações correspondestes para essa categoria')
        else:
            print('Manifestsações da categoria', pesquisar_categoria)

            for i in manifestacoes:
                print('código', i[0], 'autor', i[1], 'categoria', i[2], 'descrição', i[3], 'data e hora', i[4])

    elif op == 3:
        cod = int(input('Digite o código: '))

        pesquisar = 'select * from manifestacoes where codigo =' + str(cod)
        manifestacoes = listarBancoDados(conexao, pesquisar)

        if len(manifestacoes) == 0:
            print('Não há manifestação correspondente para esse código')
        else:
            print('A manifestação é:')

            for i in manifestacoes:
                print('código', i[0], 'autor', i[1], 'categoria', i[2], 'descrição', i[3], 'data e hora', i[4])

    elif op == 4:
        autor = input('Digite o nome de quem está fazendo a manifestação: ')
        categoria = input('Digite a categoria: ')
        descricao = input('Digite a descrição: ')

        insert = 'insert into manifestacoes(autor, categoria, descricao) values(%s,%s,%s)'
        dados = [autor, categoria, descricao]

        insertNoBancoDados(conexao, insert, dados)
        print('Manifestação adicionada')

    elif op == 5:
        codigo = int(input('Digite o código da manifestação a ser atualizada: '))
        novo_autor = input('Digite o novo autor: ')
        nova_categoria = input('Digite a nova categoria: ')
        nova_descricao = input('Digite a nova descrição: ')

        atualizar = 'update manifestacoes set autor = %s, categoria = %s, descricao = %s where codigo = %s'
        dados = [novo_autor, nova_categoria, nova_descricao, codigo]

        atualizarBancoDados(conexao, atualizar, dados)
        print('manifestação atualizada com sucesso')

    elif op == 6:
        codigo = int(input('Digite o código da manifestação que deve ser deletada: '))

        deletar = 'delete from manifestacoes where codigo = ' + str(codigo)
        dados = [codigo]

        excluirBancoDados(conexao, deletar, dados)
        print('Excluído com sucesso')

    elif op != 7:
        print('Opção inválida')

encerrarBancoDados(conexao)
print('Obrigado por usar o sistema de ouvidoria')
