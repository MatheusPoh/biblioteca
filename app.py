from flask import Flask
from routes.livro_routes import livro_bp

app = Flask(__name__)
app.register_blueprint(livro_bp)

@app.route("/")
def home():
    return "<h1>OK</h1>"

if __name__ == "__main__":
    app.run(debug=True)