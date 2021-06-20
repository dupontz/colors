import pytest
from flask import Flask
from src.app import initialize_app
from src.database import db


@pytest.fixture(scope='module')
def test_client():
    flask_app = initialize_app(Flask(__name__), config_filename='test.cfg')
    # TODO sqllite is creating "memory" file instead of using memory

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()

    yield

    db.drop_all()
