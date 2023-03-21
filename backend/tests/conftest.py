# backend/tests/conftest.py

import pytest
from backend.app import app as flask_app
from backend.app import db as _db

@pytest.fixture(scope='session')
def app():
    return flask_app

@pytest.fixture(scope='session')
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()
