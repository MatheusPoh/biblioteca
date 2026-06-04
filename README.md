Um crud básico escalonável para treinar lógica, SQLite e flask.
Objetivos incompletos ou ainda não iniciados:
  criar layout web, 
  criar sistema de cadastro de pessoas, 


    if not nome or not autor:
        return jsonify({"erro": "Dados inválidos"}), 400
    cadastrar_livro(nome, autor)

    return jsonify({"mensagem": "Livro cadastrado!"})