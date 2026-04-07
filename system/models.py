class Livros:
    def __init__(self, nome, autor, disponivel=True):
        self.nome = nome
        self.autor = autor
        self.disponivel = disponivel
    def __str__(self):
        status = "Disponivel" if self.disponivel else "Alugado"
        return f"Nome: {self.nome} | Autor: {self.autor} | Status: {status}"