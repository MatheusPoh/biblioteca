from system.models import Livros
from system.database import listar_livros_db
from system.database import inserir_livros
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
    choice = input("Qual o nome do livro que deseja alugar? ").strip().lower()
    for livro in livros:
        if livro.nome.lower() == choice:
            if livro.disponivel:
                livro.disponivel = False
                print(f"Livro \"{livro.nome}\" alugado com êxito!")
            else:
                print(f"O livro \"{livro.nome}\" Já foi alugado")
            return
    print(f"O livro \"{choice}\" não foi encontrado.")
def devolver_livro():
    devolver = input("Qual livro você deseja devolver? ").strip().lower()
    for livro in livros:
        if livro.nome.lower() == devolver:
            if not livro.disponivel:
                livro.disponivel = True
                print(f"Livro \"{livro.nome}\" devolvido com êxito!")
            else:
                print(f"O livro \"{devolver}\" já está disponível")
            return
    print(f"Livro \"{devolver}\" não encontrado.")
livros = listar_livros_db()