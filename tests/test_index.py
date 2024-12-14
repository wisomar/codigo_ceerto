import pytest
from api.index import app  # Importa o app Flask corretamente

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Testando a rota '/'
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Oi, meu nome é William!" in response.data.decode("utf-8")  # Decodifica os dados para string

# Testando uma rota inexistente
def test_404(client):
    response = client.get('/rota-inexistente')
    assert response.status_code == 404
    assert response.json == {"status": 404, "message": "Not Found"}
