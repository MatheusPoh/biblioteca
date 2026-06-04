import sqlite3
import os
from app.system.models import Livros

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data.db")

def conectar():
    return sqlite3.connect(DB_PATH)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        autor TEXT,
        disponivel BOOLEAN,
        UNIQUE(nome, autor)
    )
    """)
    conn.commit()
    conn.close()

def inserir_livros(nome, autor):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO livros (nome, autor, disponivel) VALUES (?, ?, ?)",
            (nome, autor, True)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def listar_livros_db():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, autor, disponivel FROM livros")
    dados = cursor.fetchall()
    livros = []
    for id, nome, autor, disponivel in dados:
        livros.append(Livros(id, nome, autor, bool(disponivel)))
    conn.close()
    return livros

def alugar_livro_db(livro_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 0
    WHERE id = ?
    AND disponivel = 1
    """, (livro_id,))
    alterados = cursor.rowcount

    conn.commit()
    conn.close()
    return alterados

def devolver_livro_db(livro_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 1
    WHERE id = ?
    AND disponivel =0
    """, (livro_id,))
    alterados = cursor.rowcount

    conn.commit()
    conn.close()
    return alterados

def deletar_livro_db(livro_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM livros
    WHERE id = ?
    """, (livro_id,))
    deletados = cursor.rowcount

    conn.commit()
    conn.close()
    return deletados