from fastapi import FastAPI
from routes import order_routes

app = FastAPI(
    title="Order Management API",
    description="API to manage customer orders",
    version="1.0.0",
    docs_url="/docs",     # Swagger UI
    redoc_url="/redoc"    # ReDoc UI
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI working!"}

app.include_router(order_routes)
