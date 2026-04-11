import sqlite3
import os
from system.models import Livros

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
        disponivel BOOLEAN
    )
    """)
    conn.commit()
    conn.close()

def inserir_livros(nome, autor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO livros (nome, autor, disponivel) VALUES (?, ?, ?)",
        (nome, autor, True)
    )
    conn.commit()
    conn.close()

def listar_livros_db():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, autor, disponivel FROM livros")
    dados = cursor.fetchall()
    conn.close()
    livros = []
    for nome, autor, disponivel in dados:
        livros.append(Livros(nome, autor, bool(disponivel)))
    return livros

def alugar_livro_db(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 0
    WHERE LOWER(nome) = LOWER(?)
    AND disponivel = 1
    """, (nome,))
    alterados = cursor.rowcount

    conn.commit()
    conn.close()
    return alterados

def devolver_livro_db(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE livros
    SET disponivel = 1
    WHERE LOWER(nome) = LOWER(?)
    AND disponivel =0
    """, (nome,))
    alterados = cursor.rowcount

    conn.commit()
    conn.close()
    return alterados

def deletar_livro_db(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM livros
    WHERE LOWER(nome) = LOWER(?)
    """, (nome,))
    deletados = cursor.rowcount

    conn.commit()
    conn.close()
    return deletados