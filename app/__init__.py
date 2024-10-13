import os
from flask_migrate import Migrate
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='C://Users//Petr//OneDrive//Рабочий стол//5 семестр//Работа//Project//templates')
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from .controllers import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        # Эта строка создает все таблицы в базе данных, если они не существуют
        db.create_all()

    return app
