import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate

from .database import db
from blueprints import api_blueprint

def create_app(base_dir):
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'instance/passwords.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    bcrypt = Bcrypt(app)
    migrate = Migrate(app, db)

    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
