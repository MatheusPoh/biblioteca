from app.system.database import inserir_livros ,listar_livros_db, alugar_livro_db, devolver_livro_db, deletar_livro_db

def cadastrar_livro(nome, autor):
    livros = listar_livros_db()
    for livro in livros:
        if (
            livro.nome.lower() == nome.lower() and
            livro.autor.lower() == autor.lower()
        ):
            return False

    return inserir_livros(nome, autor)

def listar_livros():
    return listar_livros_db()

def alugar_livro(livro_id):
    return alugar_livro_db(livro_id)

def devolver_livro(livro_id):
    return devolver_livro_db(livro_id)

def deletar_livro(livro_id):
    return deletar_livro_db(livro_id)