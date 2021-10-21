from fastapi.testclient import TestClient
from http import HTTPStatus
from api_orders.api import app

@pytest.fixture
def client():
    return TestClient(app)

def test_quando_verificar_integridade_deve_retornar_200():
    response = client.get("/healthcheck")
    assert response.status_code == HTTPStatus.OK

def test_quando_verificar_integridade_formato_retorno_deve_ser_json():
    response = client.get("/healthcheck")
    assert response.headers["Content-Type"] == "application/json"

def test_quando_verificar_integridade_deve_retornar_informacoes():
    response = client.get("/healthcheck")
    assert response.json() == {
        "status" : "ok"
    }
