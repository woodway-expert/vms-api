import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import get_db, Base

# Test database URL (using SQLite for testing)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "VMS API is running" in response.json()["message"]


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_currency():
    currency_data = {
        "CurrencyDate": "2024-01-01T00:00:00",
        "CourseEur": 1.0,
        "CourseUsd": 0.85,
        "CourseRub": 90.0,
        "Comments": "Test currency",
    }
    response = client.post("/api/v1/currencies/", json=currency_data)
    assert response.status_code == 200
    data = response.json()
    assert data["CourseEur"] == 1.0
    assert data["CourseUsd"] == 0.85


def test_get_currencies():
    response = client.get("/api/v1/currencies/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_customer():
    customer_data = {
        "CompanyName": "Test Company",
        "ContactName": "John Doe",
        "Phone": "123-456-7890",
        "EMail": "john@testcompany.com",
        "City": "Test City",
    }
    response = client.post("/api/v1/customers/", json=customer_data)
    assert response.status_code == 200
    data = response.json()
    assert data["CompanyName"] == "Test Company"
    assert data["ContactName"] == "John Doe"


def test_get_customers():
    response = client.get("/api/v1/customers/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
