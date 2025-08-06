import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models.user import User
from app.auth import get_password_hash

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_admin.db"

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


@pytest.fixture(scope="module")
def auth_headers():
    # Create admin user
    db = TestingSessionLocal()
    admin_user = User(
        Username="admin_user",
        Email="admin@example.com",
        HashedPassword=get_password_hash("adminpass"),
        IsAdmin=True,
    )
    db.add(admin_user)
    db.commit()

    # Log in as admin
    login_response = client.post(
        "/api/auth/login",
        data={"username": "admin_user", "password": "adminpass"},
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    yield headers

    # Clean up
    db.delete(admin_user)
    db.commit()
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_get_users_as_admin(auth_headers):
    response = client.get("/api/v1/admin/users", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_and_get_supplier(auth_headers):
    # Create a supplier
    supplier_data = {"CompanyName": "Test Supplier", "Email": "supplier@test.com"}
    response = client.post(
        "/api/v1/admin/suppliers", headers=auth_headers, json=supplier_data
    )
    assert response.status_code == 201
    created_supplier = response.json()
    assert created_supplier["CompanyName"] == "Test Supplier"

    # Get suppliers
    response = client.get("/api/v1/admin/suppliers", headers=auth_headers)
    assert response.status_code == 200
    assert any(s["CompanyName"] == "Test Supplier" for s in response.json())


def test_create_and_get_warehouse(auth_headers):
    # Create a warehouse
    warehouse_data = {"Name": "Main Warehouse", "Location": "City Center"}
    response = client.post(
        "/api/v1/admin/warehouses", headers=auth_headers, json=warehouse_data
    )
    assert response.status_code == 201
    created_warehouse = response.json()
    assert created_warehouse["Name"] == "Main Warehouse"

    # Get warehouses
    response = client.get("/api/v1/admin/warehouses", headers=auth_headers)
    assert response.status_code == 200
    assert any(w["Name"] == "Main Warehouse" for w in response.json())


def test_access_admin_routes_as_non_admin():
    # Create non-admin user
    db = TestingSessionLocal()
    non_admin_user = User(
        Username="non_admin",
        Email="nonadmin@example.com",
        HashedPassword=get_password_hash("userpass"),
        IsAdmin=False,
    )
    db.add(non_admin_user)
    db.commit()

    # Log in as non-admin
    login_response = client.post(
        "/api/auth/login",
        data={"username": "non_admin", "password": "userpass"},
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Attempt to access admin route
    response = client.get("/api/v1/admin/users", headers=headers)
    assert response.status_code == 403

    db.delete(non_admin_user)
    db.commit()
    db.close()
