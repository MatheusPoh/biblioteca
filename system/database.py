import sqlite3
from system.models import Livros
def conectar():
    return sqlite3.connect("data.db")
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
    """) #cria tabela se não existir uma com esse nome
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