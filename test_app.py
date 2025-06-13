import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(client):
    """Ստուգում է, որ գլխավոր էջը վերադարձնում է ճիշտ տեքստ։"""
    response = client.get('/')
    assert response.status_code == 200
    # Այս տեքստը պետք է ճիշտ նույնը լինի, ինչ app.py-ում
    assert b"My Awesome SI/SD Pipeline!" in response.data