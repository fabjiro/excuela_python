from flask import Flask
from .config import Config
from .extensions import db, bcrypt, jwt, migrate
from .interfaces.api.routes import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(main)
    
    return app
