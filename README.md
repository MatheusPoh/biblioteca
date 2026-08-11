# 📚 Biblioteca API

> Projeto pessoal de estudos em **constante desenvolvimento**, sem data de conclusão prevista. O objetivo não é "terminar", e sim usar este repositório como laboratório contínuo para aprender e aplicar o maior número possível de tecnologias do ecossistema de desenvolvimento de software.

![Status](https://img.shields.io/badge/status-em%20desenvolvimento%20cont%C3%ADnuo-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Flask](https://img.shields.io/badge/flask-REST%20API-black)
![License](https://img.shields.io/badge/licen%C3%A7a-MIT-lightgrey)

---

## 📖 Sobre o projeto

O **Biblioteca API** é um sistema de gerenciamento de livros (cadastro, aluguel, devolução e remoção) que nasceu como um **CRUD via linha de comando (CLI)** e evoluiu para uma **API REST** construída com Flask, com uma pequena interface web para consumir os endpoints.

Este projeto é, antes de tudo, **um espaço de aprendizado**. Não há prazo de entrega, não há escopo fechado — a ideia é ir incrementando funcionalidades, boas práticas e tecnologias novas conforme eu evoluo como desenvolvedor. Por isso é normal encontrar aqui código sendo refatorado, features experimentais e partes que ainda vão mudar bastante.

Se você chegou até este repositório: sinta-se à vontade para acompanhar a evolução, abrir issues ou sugerir melhorias.

---

## 🧠 Motivação e histórico

- **v0 — CLI CRUD:** primeira versão, um CRUD simples rodando no terminal, focado em fixar lógica de programação, estruturas de dados e persistência.
- **v1 — API REST (atual):** migração da lógica para uma API construída com Flask, separando responsabilidades em camadas (rotas, serviços e acesso a dados) e adicionando uma interface web básica para testar os endpoints.
- **Próximas versões:** o plano é ir incorporando gradualmente autenticação, banco de dados relacional mais robusto, containerização, testes automatizados, documentação interativa e, possivelmente, um front-end mais completo.

---

## 🛠️ Tecnologias utilizadas atualmente

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3 |
| Framework web / API | Flask |
| CORS | Flask-CORS |
| Banco de dados | SQLite (via `sqlite3`) |
| Front-end (interface de teste) | HTML5, CSS3, JavaScript (Vanilla) |
| Arquitetura | Application Factory Pattern (Flask), Blueprints, camadas de rotas/serviços/dados |

## 🚀 Tecnologias e conceitos no radar (roadmap de aprendizado)

Como o objetivo é agregar o máximo de tecnologias possível ao longo do tempo, estes são alguns dos próximos aprendizados planejados para o projeto:

- [ ] ORM (SQLAlchemy) no lugar de SQL puro
- [ ] Migração para PostgreSQL / MySQL
- [ ] Autenticação e autorização (JWT)
- [ ] Documentação interativa da API (Swagger / OpenAPI)
- [ ] Testes automatizados (Pytest)
- [ ] Containerização com Docker / Docker Compose
- [ ] CI/CD (GitHub Actions)
- [ ] Variáveis de ambiente e configuração por ambiente (dev/prod)
- [ ] Logging estruturado
- [ ] Front-end em framework moderno (React ou similar)
- [ ] Deploy em nuvem

---

## 📂 Estrutura do projeto

```
biblioteca/
├── app/
│   ├── app.py                  # Application factory (cria e configura o Flask app)
│   ├── routes/
│   │   └── livro_routes.py     # Endpoints da API (Blueprint de livros)
│   ├── services/
│   │   └── livro_service.py    # Regras de negócio
│   ├── system/
│   │   ├── database.py         # Conexão e operações no SQLite
│   │   └── models.py           # Modelo de dados (Livro)
│   ├── static/                 # CSS e JS da interface de teste
│   └── templates/              # HTML da interface de teste
├── run.py                      # Ponto de entrada da aplicação
└── README.md
```

---

## 📡 Endpoints da API

| Método | Rota | Descrição | Body (JSON) |
|---|---|---|---|
| `GET` | `/livros` | Lista todos os livros cadastrados | — |
| `POST` | `/livros` | Cadastra um novo livro | `{ "nome": "string", "autor": "string" }` |
| `PUT` | `/livros/alugar` | Marca um livro como alugado | `{ "id": int }` |
| `PUT` | `/livros/devolver` | Marca um livro como devolvido/disponível | `{ "id": int }` |
| `DELETE` | `/livros/deletar` | Remove um livro do acervo | `{ "id": int }` |

---

## ▶️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/MatheusPoh/biblioteca.git
cd biblioteca

# Crie e ative um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# Instale as dependências
pip install flask flask-cors

# Execute a aplicação
python run.py
```

A aplicação sobe em `http://127.0.0.1:5000`, onde a interface de teste consome a API. O banco SQLite (`data.db`) é criado automaticamente na primeira execução.

---

## ⚠️ Status do projeto

Este é um projeto **de estudo, sem data de término**. Funcionalidades podem ser adicionadas, removidas ou reescritas a qualquer momento conforme novos conceitos forem sendo aprendidos e aplicados. Use como referência de aprendizado, não como software pronto para produção (ainda).

## 📄 Licença

Distribuído sob a licença MIT. Sinta-se livre para estudar, usar como referência e sugerir melhorias.
