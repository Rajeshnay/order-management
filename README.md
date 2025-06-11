#  Order Management System (FastAPI + PostgreSQL)

A production-ready backend microservice for managing customer orders, built using **FastAPI**, **PostgreSQL**, and **Docker**. This system supports full CRUD operations on orders and can be easily extended for real-world e-commerce platforms.



##  Features

-  Create, Read, Update, and Delete Orders
-  Pagination and filtering support
-  RESTful API design with validation
-  Unit testing for core logic
-  Dockerized for easy deployment
-  Deployed on Render.com



## Tech Stack

| Component       | Technology         |
|----------------|--------------------|
| Backend         | Python (FastAPI)   |
| Database        | PostgreSQL         |
| API Docs        | Swagger UI (`/docs`) |
| Testing         | Pytest             |
| Containerization| Docker             |
| Deployment      | Render             |



##  Setup Instructions

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker (optional but recommended)

###  Clone the Repository

```bash
git clone https://github.com/Rajeshnay/order-management.git
cd order-management

#  Setup Environment Variables
Create a .env file:
DATABASE_URL=postgresql://username:password@localhost:5432/orders_db
### Run Locally (without Docker)
pip install -r requirements.txt
uvicorn main:app --reload
API will be available at: http://localhost:8000/docs

## Run with Docker
docker build -t order-management .
docker run -d -p 8000:8000 order-management

## API Endpoints
Method	Endpoint	Description
GET	/	Welcome message
POST	/orders/	Create a new order
GET	/orders/{order_id}	Get an order by ID
PUT	/orders/{order_id}	Update an order
DELETE	/orders/{order_id}	Del

##API Documentation


Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## Deployed URL
Live Swagger API Docs:
🔗 https://order-management-ueav.onrender.com/docs

## Notes
The project includes unit tests for critical functionalities.
PostgreSQL must be running and accessible with correct credentials.
API Gateway and Service Discovery are not implemented as they are not essential for a single-service architecture.

