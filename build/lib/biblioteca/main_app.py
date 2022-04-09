from classes import Livro

livros = []

while True:

    print("BIBLIOTECA DIGITAL")

    print("Escolha uma opção")

    menu = int(input("1 - Consultar acervo, 2 - Adicionar livro ao acervo, 3 - Sair "))

    if menu == 2:
        print("Insira um livro para cadastrar")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano de publicação: ")
        genero = input("Gênero: ")
        sinopse = input("Sinopse: ")

        new_livro = Livro(titulo, autor, ano, genero, sinopse)

        print("Livro adicionado:")
        print(f'Nome: {new_livro.titulo}')
        print(f'Autor: {new_livro.autor}')
        print(f'Ano: {new_livro.ano}')
        print(f'Genero: {new_livro.genero}')
        print(f'Sinopse: {new_livro.sinopse}')

        livros.append(new_livro.titulo)
        menu2 = int(input("1 - Voltar para o menu, 2 - Adicionar novo livro, 3 - Encerrar aplicação"))

        if menu2 == 2:
            continue

        elif menu2 == 3:
            break

    elif menu == 1:

            print(livros)

    elif menu == 3:
            break