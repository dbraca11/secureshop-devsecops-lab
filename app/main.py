from fastapi import FastAPI, HTTPException, Request

app = FastAPI(title="SecureShop API")

products = [
    {"id": 1, "name": "Laptop", "price": 1200.00},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Headphones", "price": 150.00}
]
orders = []

@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = "default-src 'self'; frame-ancestors 'none';"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to SecureShop API"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "secureshop-api"}

@app.get("/products")
def get_products():
    return {"products": products}

@app.post("/orders", status_code=201)
def create_order(order: dict):
    product_id = order.get("product_id")
    quantity = order.get("quantity", 1)
    
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    total_price = product["price"] * quantity
    new_order = {
        "id": len(orders) + 1, 
        "product_id": product_id, 
        "quantity": quantity,
        "total_price": total_price
    }
    orders.append(new_order)
    return new_order

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = next((o for o in orders if o["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
