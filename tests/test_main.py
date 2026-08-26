from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "secureshop-api"}

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert "products" in response.json()
    assert len(response.json()["products"]) == 3

def test_create_and_get_order():
    response_create = client.post("/orders", json={"product_id": 1, "quantity": 2})
    assert response_create.status_code == 201
    data = response_create.json()
    assert data["id"] == 1
    assert data["total_price"] == 2400.00

    response_get = client.get("/orders/1")
    assert response_get.status_code == 200
    assert response_get.json()["id"] == 1

def test_create_order_invalid_product():
    response = client.post("/orders", json={"product_id": 999, "quantity": 1})
    assert response.status_code == 404
