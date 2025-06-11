from pydantic import BaseModel, ConfigDict
from typing import Optional

# 👇 This must exist
class OrderCreate(BaseModel):
    customer_name: str
    item_name: str
    quantity: int

# 👇 This must also exist if you're using OrderResponse
class OrderResponse(BaseModel):
    id: int
    customer_name: str
    item_name: str
    quantity: int
    status: str

    model_config = ConfigDict(from_attributes=True)

class OrderUpdate(BaseModel):
    status: str

    model_config = ConfigDict(from_attributes=True)