import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models.user import User
from app.auth import get_password_hash

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


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    # Create a test user
    user = User(
        Username="testuser",
        Email="testuser@example.com",
        HashedPassword=get_password_hash("testpassword"),
        IsAdmin=True,
    )
    db.add(user)
    db.commit()
    yield db
    Base.metadata.drop_all(bind=engine)


def test_login_for_access_token(test_db):
    response = client.post(
        "/api/auth/login",
        data={"username": "testuser", "password": "testpassword"},
    )
    assert response.status_code == 200
    json_response = response.json()
    assert "access_token" in json_response
    assert json_response["token_type"] == "bearer"


def test_login_for_access_token_invalid_credentials(test_db):
    response = client.post(
        "/api/auth/login",
        data={"username": "wronguser", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


def test_read_users_me(test_db):
    login_response = client.post(
        "/api/auth/login",
        data={"username": "testuser", "password": "testpassword"},
    )
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/api/auth/users/me", headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["Username"] == "testuser"
    assert json_response["Email"] == "testuser@example.com"
