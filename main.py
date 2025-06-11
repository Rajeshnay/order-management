from fastapi import FastAPI
from routes import order_routes

app = FastAPI( 
    title="Order Management API",
    version="1.0",
    docs_url="/docs",         # Swagger UI
    redoc_url="/redoc",       # ReDoc UI
    openapi_url="/openapi.json"  # OpenAPI schema
      )

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI working!"}

app.include_router(order_routes, prefix="/api", tags=["Orders"])
