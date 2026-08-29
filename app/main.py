from fastapi import FastAPI, Request

app = FastAPI(title="SecureShop API")

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
    return {"status": "healthy"}
