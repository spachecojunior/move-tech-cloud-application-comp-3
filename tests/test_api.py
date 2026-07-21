from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_criar_e_listar_pedido():
    r = client.post("/orders", json={"customer": "Teste CI"})
    assert r.status_code == 201
    pedido = r.json()
    assert pedido["customer"] == "Teste CI"
    assert pedido["status"] == "open"

    r2 = client.get("/orders")
    assert r2.status_code == 200
    assert any(p["id"] == pedido["id"] for p in r2.json())
