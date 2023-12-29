lista_livro = []
id_global = 0
print('Bem-vindo ao controle de livros do Pablo Ramon Galdino Barros')

def cadastra_livro():
    id = id_global + 1
    print('-' * 25, 'Cadastro de Livros', '-' * 25)
    print('ID do livro -', id)
    nome = input('Nome do livro: ')
    autor = input('Nome do(a) autor(a): ')
    editora = input('Editora: ')
    livro = {'id': id, 'Nome': nome, 'Autor(a)': autor, 'Editora': editora}
    lista_livro.append(livro)
    print()
    print('Livro cadastrado com sucesso!')


def consultar_livro():
    if lista_livro:
        try:
            for i, livro in enumerate(lista_livro, 1):
                print('ID: {}\nNome: {}\nAutor(a): {}\nEditora: {}'
                    .format(i, livro['Nome'], livro['Autor(a)'], livro['Editora']))
                print()
        except:
            print('Erro!')
    else:
        print('Nenhum livro encontrado.')

def remove_livro():
    if lista_livro:
        rmv_id = int(input('Id do livro a ser removido: '))
        #Verifica de o id esta entre 1 e o tamanho final da lista. Se sim l
        if 1 <= rmv_id <= len(lista_livro):
            livro = lista_livro.pop(rmv_id - 1)
            print('O livro ({}) foi removido com sucesso!'.format(livro['Nome']))
        else:
            print('Id inválido\nO id não corresponde a nenhum livro cadastrado.')
    else:
        print('Não há livro para remover.')

#Programa Principal
while True:
    print('-' * 25, 'MENU PRINCIPAL', '-' * 25)
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro')
    print('3 - Remover Livro')
    print('4 - Encerrar o Programa')
    e = input('Escolha a opção desejada: ')
    print()

    if e == '1':
        cadastra_livro()
        id_global += 1
    elif e == '2':
        while True:
            print('-' * 25, 'Consulta de Livros', '-' * 25)
            print('1 - Consultar todos')
            print('2 - Consultar por id')
            print('3 - Consultar por autor(a)')
            print('4 - Retornar ao menu principal')
            e2 = input('Escolha a opção desejada: ')
            print()
            if e2 == '1':
                consultar_livro()
            elif e2 == '2':
                if lista_livro:
                    try:
                        id_livro = int(input('Qual o id do livro? '))
                        #verifica se o id inserido está entre 1 e o tamanho da lista
                        if 1 <= id_livro <= len(lista_livro):
                            livro = lista_livro[id_livro - 1]
                            print('ID: {}\nNome: {}\nAutor(a): {}\nEditora: {}'
                                    .format(id_livro, livro['Nome'], livro['Autor(a)'], livro['Editora']))
                            print()
                        else:
                            print('Id Inválido.\nO id não correspode a nenhum livro cadastrado.')
                    except:
                        print('Por favor, digite apenas números.')
                else:
                    print('Nenhum livro encontrado.')

            elif e2 == '3':
                if lista_livro:
                    autor = input('Digite o nome do(a) autor(a): ')
                    livros_autor = [livro for livro in lista_livro if livro['Autor(a)'].lower() == autor.lower()]
                    if livros_autor:
                        for livro in livros_autor:
                            print('id: {}\nNome: {}\nAutor(a): {}\nEditora: {}'
                                  .format(livro['id'], livro['Nome'], livro['Autor(a)'], livro['Editora']))
                            print()
                    else:
                        print('Nenhum livro encontrado para esse autor.')
                else:
                    print('Nenhum livro encontrado.')
            elif e2 == '4':
                break
            else:
                print('Opção Inválida!')
    elif e == '3':
        remove_livro()
        print()

    elif e == '4':
        print('Encerrando o programa...')
        break
