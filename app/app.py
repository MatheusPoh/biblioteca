import ipaddress
from flask import Flask,render_template,request
from app.routes.livro_routes import livro_bp
from flask_cors import CORS
from app.system.database import criar_tabela

def get_ip():
    ip = request.headers.get("X-Forwarded-For")

    if ip:
        # pega o primeiro IP da lista
        ip = ip.split(",")[0].strip()

        # trata IPv4 dentro de IPv6
        if ip.startswith("::ffff:"):
            ip = ip.replace("::ffff:", "")

    else:
        ip = request.remote_addr

    # valida IP
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return "IP inválido"

    return ip

    return request.remote_addr
def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    CORS(app, origins="http://127.0.0.1:5000")
    criar_tabela()
    app.register_blueprint(livro_bp)

    @app.route("/")
    def home():
        ip = get_ip()
        print("IP: ", ip)
        return render_template("index.html")

    return app