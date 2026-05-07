import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from app.extensions.db import db, migrate
from app.models import Task, TaskHistory
from app.api.routes.task_routes import task_bp

load_dotenv()


def create_app():
    app = Flask(__name__)

    database_url = os.getenv("DATABASE_URL")

    if database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg2://",
            1,
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return {"message": "FlowBoard API running"}

    app.register_blueprint(task_bp, url_prefix="/api")
    return app