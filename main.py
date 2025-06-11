from fastapi import FastAPI
from routes import order_routes

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI working!"}

app.include_router(order_routes)
