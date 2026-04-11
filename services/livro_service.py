from system.database import inserir_livros ,listar_livros_db, alugar_livro_db, devolver_livro_db, deletar_livro_db

def cadastrar_livro():
    livros = listar_livros_db()

    nome = input("Nome do livro: ").strip()
    autor = input("Autor: ").strip()

    if not nome or not autor:
        print("Nome e autor são obrigatórios.")
        return
    for livro in livros:
        if livro.nome.lower() == nome.lower():
            print("Esse livro já existe!")
            return

    inserir_livros(nome, autor)
    print("livro cadastrado com sucesso!")


def listar_livros():
    livros = listar_livros_db()

    if not livros:
        print("A lista está vazia!")
        return
    for livro in livros:
        print(livro)


def emprestar_livro():
    nome = input("Qual o nome do livro que deseja alugar? ").strip().lower()
    resultado = alugar_livro_db(nome)

    if resultado:
        print(f"Livro \"{nome}\" emprestado com sucesso!")
    else:
        print("Livro não encontrado ou já emprestado.")


def devolver_livro():
    nome = input("Qual livro você deseja devolver? ").strip().lower()
    resultado = devolver_livro_db(nome)

    if resultado:
        print(f"Livro \"{nome}\" devolvido com sucesso!")
    else:
        print("Livro não encontrado ou não alugado.")

def deletar_livro():
    nome = input("Qual livro você deseja deletar? ").strip().lower()
    resultado = deletar_livro_db(nome)

    if resultado:
        print(f"Livro \"{nome}\" deletado com sucesso!")
    else:
        print("Livro não encontrado.")