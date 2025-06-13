import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):

    response = client.get('/')
    assert response.status_code == 200

    assert b"My Awesome SI/SD Pipeline!" in response.data