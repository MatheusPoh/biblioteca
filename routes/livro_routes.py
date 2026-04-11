from flask import Blueprint, request, jsonify
from system.database import inserir_livros, listar_livros_db, alugar_livro_db, devolver_livro_db, deletar_livro_db

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

@livro_bp.route("/livros/alugar", methods=["PUT"])
def alugar():
    dados = request.json
    nome = dados.get("nome")

    if not nome:
        return jsonify({"erro": "Nome é obrigatório"}), 400

    resultado = alugar_livro_db(nome)
    if resultado:
        return jsonify({"mensagem": "Livro alugado com êxito!"})
    else:
        return jsonify({"erro": "Livro não encontrado ou já alugado."}), 404

@livro_bp.route("/livros/devolver", methods=["PUT"])
def devolver():
    dados = request.json
    nome = dados.get("nome")

    if not nome:
        return jsonify({"erro": "Nome é obrigatório"}), 400

    resultado = devolver_livro_db(nome)
    if resultado:
        return jsonify({"mensagem": "Livro devolvido com êxito!"})
    else:
        return jsonify({"erro": "Livro não encontrado ou já devolvido."}), 404

@livro_bp.route("/livros/deletar", methods=["DELETE"])
def deletar():
    dados = request.json
    nome = dados.get("nome")

    if not nome:
        return jsonify({"erro": "Nome é obrigatório."}), 400

    resultado = deletar_livro_db(nome)
    if resultado:
        return jsonify({"mensagem": "Livro deletado com êxito!"})
    else:
        return jsonify({"erro": "Livro não encontrado."}), 404