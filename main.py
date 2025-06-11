from fastapi import FastAPI
from routes import order_routes

app = FastAPI(
    title="Order Management API",
    description="API for managing orders using FastAPI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI working!"}

app.include_router(order_routes)
