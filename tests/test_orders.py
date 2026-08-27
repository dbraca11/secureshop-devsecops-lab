from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_order_missing_product():
    response = client.post("/orders", json={"product_id": 999, "quantity": 1})
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}
