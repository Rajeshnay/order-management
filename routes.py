from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db  # your DB session dependency
from models import Order, OrderStatus
from schemas import OrderCreate, OrderResponse,OrderUpdate

order_routes = APIRouter()

# Create Order
@order_routes.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(
        customer_name=order.customer_name,
        item_name=order.item_name,  # if your model uses item_name
        quantity=order.quantity,
        status=OrderStatus.PENDING,
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Read single Order by ID
@order_routes.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


# Update Order by ID
@order_routes.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    db_order.status = order_update.status
    db.commit()
    db.refresh(db_order)
    return db_order

# Delete Order by ID
@order_routes.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(db_order)
    db.commit()
    return {"detail": f"Order {order_id} deleted successfully"}
