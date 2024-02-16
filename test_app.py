import pytest

from app import create_app
from route import bp
from flask import Flask

@pytest.fixture

def client():
    app = create_app()

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_status(client):
    response = client.get('/combat')
    assert response.status_code == 200