from projetos_de_banco_de_dados.cadastro_de_nomes.cadastro_nomes_simples import banco_d_dados

#===================================================================

while True:
    print(f'''Menu de Opções:
[ 1 ] Para adicionar um novo nome
[ 2 ] Para alterar um nome existente
[ 3 ] Para visualizar nomes cadastrados
[ 4 ] Para excluir nomes
[ 5 ] Sair''')

#===================================================================

    escolha = input('Escolha uma das opções: ')

    if escolha == '1':
        chave = input('Digite a sua chave para um novo nome: ')
        nome = input('Digite o nome que deseja armazenar: ')
        banco_d_dados[chave] = nome
        print(f'O nome {nome} foi associado com a chave {chave}.')

#===================================================================

    elif escolha == '2':
        chave = input('Digite a chave do nome que deseja alterar: ')
        if chave in banco_d_dados:
            novo_nome = input('Digite o nome novo: ')
            banco_d_dados[chave] = novo_nome
            print(f'O nome {novo_nome} agora está associado a chave {chave}')

        else:
            print(f'Chave "{chave}" não encontrada.')

#===================================================================

    elif escolha == '3':
        if banco_d_dados:
            print('\nNomes Armazenados:')
            for chave, nome in banco_d_dados.items():
                print(f'''Chave: {chave}
Nome: {nome}''')
        else:
            print('Nenhum nome armazenado.')

#===================================================================

    elif escolha == '4':
        chave = input('Digite a chave do nome que deseja excluir: ')
        if chave in banco_d_dados:
            del banco_d_dados[chave]
            print(f'O nome associado a chave "{chave}" foi excluído.')

        else:
            print(f'Chave {chave} não encontrada.')

#===================================================================

    elif escolha == '5':
        print('Fechando programa.')
        break

    else:
        print('Opção inválida.')

