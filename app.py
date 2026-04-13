from flask import Flask,render_template
from routes.livro_routes import livro_bp
from flask_cors import CORS
from system.database import criar_tabela

app = Flask(__name__)
CORS(app)
criar_tabela()
app.register_blueprint(livro_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)