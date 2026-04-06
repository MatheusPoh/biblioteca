from system.models import Livros
livros = []
def cadastrar_livro():
    nome = input("Nome do livro: ").strip()
    autor = input("Autor: ").strip()
    if not nome or not autor:
        print("Nome e autor são obrigatórios.")
        return
    for livro in livros:
        if livro.nome.lower() == nome.lower():
            print("Esse livro já existe!")
            return
    novo_livro = Livros(nome, autor)
    livros.append(novo_livro)
    print("livro cadastrado com sucesso!")