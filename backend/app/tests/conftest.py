import os
import pytest

from app import create_app
from app.extensions.db import db


@pytest.fixture
def app():
    os.environ["DATABASE_URL"] = (
        os.getenv("DATABASE_URL")
    )

    app = create_app()

    app.config.update({
        "TESTING": True,
    })

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()