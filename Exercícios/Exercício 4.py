#INICIO
lista_livro = []  #lista vazia
id_global = 0  #variável

#boas vindas
print('Bem-vindo à Livraria da Isabela Premoli')

while True:
    print('-' * 32)
    print('-' * 8, 'MENU PRINCIPAL', '-' * 8)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar livro')
    print('2 - Consultar livro')
    print('3 - Remover livro')
    print('4 - Sair')

    opcao = input('>> ')

    #função para cadastrar livros
    def cadastrar_livro():
        global id_global
        id_global += 1
        print('-' * 32)
        print('-' * 5, 'MENU CADASTRAR LIVRO', '-' * 5)
        print(f'Id do livro: {id_global}')
        
        nome = input('Por favor, entre com o nome do livro: ')
        autor = input('Por favor, entre com o nome do autor: ')
        editora = input('Por favor, entre com o nome da editora: ')
        print('-' * 32)
        print('')

        #dicionário
        livro = {
            'id': id_global,
            'nome': nome,
            'autor': autor,
            'editora': editora
        }
        
        lista_livro.append(livro)  #dicionário dentro da lista_livro

    #função para consultar livros
    def consultar_livro():
        print('-' * 32)
        print('-' * 5, 'MENU CONSULTAR LIVRO', '-' * 5)
        
        while True:
            print('Escolha a opção desejada:')
            print('1. Consultar Todos')
            print('2. Consultar por Id')
            print('3. Consultar por Autor')
            print('4. Retornar ao menu')

            opcao_consulta = input('>> ')
            print('-' * 32)

            if opcao_consulta == '1':  # Consulta todos os livros
                for livro in lista_livro:
                    print(f"id: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print('-' * 32)

            elif opcao_consulta == '2':  # Consulta por ID
                id_pesquisa = int(input("Digite o id do livro: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_pesquisa:
                        print(f"id: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        print('-' * 32)
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro não encontrado.")

            elif opcao_consulta == '3':  # Consulta por Autor
                autor_pesquisa = input("Digite o autor do(s) livro(s): ")
                encontrado = False
                for livro in lista_livro:
                    if livro['autor'] == autor_pesquisa:
                        print(f"id: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        print('-' * 32)
                        encontrado = True
                if not encontrado:
                    print("Nenhum livro encontrado para este autor.")

            elif opcao_consulta == '4':
                break

    #função para remover livro
    def remover_livro():
        id_remover = int(input("Digite o id do livro a ser removido: "))
        for livro in lista_livro:
            if livro['id'] == id_remover:
                lista_livro.remove(livro)
                print("Livro removido com sucesso!")

    #menu principal
    if opcao == '1':
        cadastrar_livro()
    elif opcao == '2':
        consultar_livro()
    elif opcao == '3':
        remover_livro()
    elif opcao == '4':
        break

#FIM