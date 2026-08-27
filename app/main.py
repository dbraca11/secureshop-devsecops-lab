from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import os

app = FastAPI(title="SecureShop API", version="0.1.0")

PRODUCTS = [
    {"id": 1, "name": "Laptop Pro", "price": 1200.00},
    {"id": 2, "name": "Wireless Mouse", "price": 25.00},
    {"id": 3, "name": "Mechanical Keyboard", "price": 80.00}
]

ORDERS: Dict[int, dict] = {}

class OrderCreate(BaseModel):
    product_id: int
    quantity: int

@app.get("/health")
def get_health():
    return {"status": "healthy", "service": "secureshop-api"}

@app.get("/products")
def get_products():
    return {"products": PRODUCTS}

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    product = next((p for p in PRODUCTS if p["id"] == order.product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    order_id = len(ORDERS) + 1
    total_price = product["price"] * order.quantity
    new_order = {
        "id": order_id,
        "product_id": order.product_id,
        "product_name": product["name"],
        "quantity": order.quantity,
        "total_price": total_price,
        "status": "created"
    }
    ORDERS[order_id] = new_order
    return new_order

@app.get(
    "/orders/{order_id}",
    responses={
        200: {"description": "Orden encontrada con éxito"},
        404: {"description": "Order not found"}
    }
)
def get_order(order_id: int):
    order = ORDERS.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

if __name__ == "__main__":
    import uvicorn
    # Solución al Blocker de SonarCloud: Evitar exponer por defecto a 0.0.0.0
    host_ip = os.getenv("HOST", "127.0.0.1")
    uvicorn.run(app, host=host_ip, port=8000)
