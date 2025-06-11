import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    response = client.post(
        "/orders/",
        json={"customer_name": "Test User", "item_name": "Test Item", "quantity": 5}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Test User"
    assert data["item_name"] == "Test Item"
    assert data["quantity"] == 5
    assert "id" in data

def test_get_order():
    # First create an order to get its ID
    create_resp = client.post(
        "/orders/",
        json={"customer_name": "Alice", "item_name": "Book", "quantity": 2}
    )
    order_id = create_resp.json()["id"]

    # Now get the order by ID
    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["customer_name"] == "Alice"

def test_get_order_not_found():
    response = client.get("/orders/9999999")  # Assuming this ID doesn't exist
    assert response.status_code == 404

def test_update_order():
    # Create an order first
    create_resp = client.post(
        "/orders/",
        json={"customer_name": "Bob", "item_name": "Pen", "quantity": 10}
    )
    order_id = create_resp.json()["id"]

    # Update order status
    response = client.put(
        f"/orders/{order_id}",
        json={"status": "SHIPPED"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"].upper() == "SHIPPED"


def test_delete_order():
    # Create an order to delete
    create_resp = client.post(
        "/orders/",
        json={"customer_name": "Eve", "item_name": "Notebook", "quantity": 1}
    )
    order_id = create_resp.json()["id"]

    # Delete the order
    response = client.delete(f"/orders/{order_id}")
    assert response.status_code == 200

    # Confirm deletion by trying to get the order
    get_resp = client.get(f"/orders/{order_id}")
    assert get_resp.status_code == 404
