from flask import Blueprint, request, jsonify
from app.services.livro_service import alugar_livro, listar_livros, cadastrar_livro, deletar_livro, devolver_livro

livro_bp = Blueprint("livros", __name__)

@livro_bp.route("/livros", methods=["GET"])
def listar():
    livros = listar_livros()

    resultado = []
    for livro in livros:
        resultado.append({
            "id": livro.id,
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

    resultado = cadastrar_livro(nome, autor)
    if resultado:
        return jsonify({"mensagem": "Livro cadastrado!"})
    else:
        return jsonify({"erro": "Livro já existente."}), 400

@livro_bp.route("/livros/alugar", methods=["PUT"])
def alugar():
    dados = request.get_json()

    try:
        livro_id = int(dados.get("id"))
    except (TypeError, ValueError):
        return jsonify({"erro": "ID inválido"}), 400

    resultado = alugar_livro(livro_id)

    if resultado:
        return jsonify({"mensagem": "Livro alugado!"})
    else:
        return jsonify({"erro": "Livro não encontrado ou já alugado"}), 400

@livro_bp.route("/livros/devolver", methods=["PUT"])
def devolver():
    dados = request.json
    try:
        livro_id = int(dados.get("id"))
    except (TypeError, ValueError):
        return jsonify({"erro": "ID inválido"}), 400

    resultado = devolver_livro(livro_id)
    if resultado:
        return jsonify({"mensagem": "Livro devolvido com êxito!"})
    else:
        return jsonify({"erro": "Livro não encontrado ou já devolvido."}), 404

@livro_bp.route("/livros/deletar", methods=["DELETE"])
def deletar():
    dados = request.get_json()

    #print("DADOS RECEBIDOS:", dados)
    #print("ID BRUTO:", dados.get("id"))

    try:
        livro_id = int(dados.get("id"))
    except (TypeError, ValueError):
        return jsonify({"erro": "ID inválido"}), 400

    resultado = deletar_livro(livro_id)

    if resultado:
        return jsonify({"mensagem": "Livro deletado!"})
    else:
        return jsonify({"erro": "Livro não encontrado"}), 404