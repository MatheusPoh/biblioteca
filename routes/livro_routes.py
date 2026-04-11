from flask import Blueprint, request, jsonify
from system.database import inserir_livros, listar_livros_db
from system.models import Livros

livro_bp = Blueprint("livros", __name__)

@livro_bp.route("/livros", methods=["GET"])
def listar():
    livros = listar_livros_db()

    resultado = []
    for livro in livros:
        resultado.append({
            "nome": livro.nome,
            "autor": livro.autor,
            "disponivel": livro.disponivel
        })
    return jsonify(resultado)

@livro_bp.route("/livros", methods=["POST"])
def cadastrar():
    dados = request.json
    nome = dados.get("nome")
    autor = dados.get("autor")

    if not nome or not autor:
        return jsonify({"erro": "Dados inválidos"}), 400
    inserir_livros(nome, autor)

    return jsonify({"mensagem": "Livro cadastrado!"})