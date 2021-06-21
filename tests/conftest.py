import pytest
from flask import Flask
from src import create_app
from src.database import db


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(config_filename='test.cfg')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client


@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()

    yield

    db.drop_all()
