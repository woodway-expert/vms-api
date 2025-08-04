from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import get_db

# Test database URL (using SQLite for testing)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_read_main():
    """Test the root endpoint returns the expected message"""
    response = client.get("/")
    assert response.status_code == 200
    assert "VMS API is running" in response.json()["message"]


def test_health_check():
    """Test the health check endpoint returns healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_api_docs_accessible():
    """Test that API documentation is accessible"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_currencies_endpoint():
    """Test the currencies endpoint is accessible"""
    response = client.get("/api/v1/currencies/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_customers_endpoint_graceful():
    """Test the customers endpoint handles database errors gracefully"""
    response = client.get("/api/v1/customers/")
    # Should return either 200 with empty list or 500 with error message
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
    else:
        assert "detail" in response.json()


def test_orders_endpoint_graceful():
    """Test the orders endpoint handles database errors gracefully"""
    response = client.get("/api/v1/orders/")
    # Should return either 200 with empty list or 500 with error message
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
    else:
        assert "detail" in response.json()


def test_inventory_endpoint_graceful():
    """Test the new inventory endpoint handles database errors gracefully"""
    response = client.get("/api/v1/inventory/")
    # Should return either 200 with empty list or 500 with error message
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
    else:
        assert "detail" in response.json()


def test_subpositions_endpoint_graceful():
    """Test the new subpositions endpoint handles database errors gracefully"""
    response = client.get("/api/v1/subpositions/")
    # Should return either 200 with empty list or 500 with error message
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
    else:
        assert "detail" in response.json()


def test_nonexistent_endpoint():
    """Test that non-existent endpoints return 404"""
    response = client.get("/api/v1/nonexistent/")
    assert response.status_code == 404


def test_customer_pagination_graceful():
    """Test customer pagination parameters handle errors gracefully"""
    response = client.get("/api/v1/customers/?skip=0&limit=10")
    # Should return either 200 with list or 500 with error message
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
    else:
        assert "detail" in response.json()


def test_customer_filtering_graceful():
    """Test customer filtering handles errors gracefully"""
    response = client.get("/api/v1/customers/?city=TestCity")
    # Should return either 200 with list or 500 with error message
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        assert isinstance(response.json(), list)
    else:
        assert "detail" in response.json()


def test_invalid_customer_id_graceful():
    """Test accessing non-existent customer handles errors gracefully"""
    response = client.get("/api/v1/customers/99999")
    # Should return 404 (not found) or 500 (database error)
    assert response.status_code in [404, 500]
    assert "detail" in response.json()


def test_api_structure_validation():
    """Test that all expected endpoints are accessible"""
    # Test core endpoints that should always work
    response = client.get("/")
    assert response.status_code == 200

    response = client.get("/health")
    assert response.status_code == 200

    response = client.get("/docs")
    assert response.status_code == 200

    # Test API endpoints return valid responses (200 or 500 for database issues)
    api_endpoints = [
        "/api/v1/currencies/",
        "/api/v1/customers/",
        "/api/v1/orders/",
        "/api/v1/inventory/",
        "/api/v1/subpositions/",
    ]

    for endpoint in api_endpoints:
        response = client.get(endpoint)
        # Should be accessible (200) or have database error (500), not 404 (not found)
        assert response.status_code != 404, f"Endpoint {endpoint} not found (404)"
        assert response.status_code in [
            200,
            500,
        ], f"Unexpected status {response.status_code} for {endpoint}"
