# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Replace the values below with your actual PostgreSQL settings
DATABASE_URL = "postgresql://postgres:Rajesh987@localhost/order_management"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
def init_db():
    Base.metadata.create_all(bind=engine)
