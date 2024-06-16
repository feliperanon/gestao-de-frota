from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)

    # Configuração do ambiente (desenvolvimento/produção)
    app.config.from_object('config.Config')  # Use um arquivo de configuração separado

    db.init_app(app)
    csrf.init_app(app)

    # Importar o blueprint depois de criar o app
    from .routes import bp
    app.register_blueprint(bp)

    return app




