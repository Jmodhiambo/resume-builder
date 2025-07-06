#!/usr/bin/env python3

"""This sets up your app instance, config, and Blueprints."""

from flask import Flask
from app.utils import db, csrf, login_manager
from config import Config
from dotenv import load_dotenv
from app.models import User

load_dotenv()

def create_app(config_class=Config):
    """Flask App Factory"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.main import main_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.resume_routes import resume_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)

    return app
