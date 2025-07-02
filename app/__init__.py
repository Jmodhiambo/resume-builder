#!/usr/bin/env python3

"""This sets up your app instance, config, and Blueprints."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

def create_app():
    """Flask App Factory"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.resume_routes import resume_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)

    return app
