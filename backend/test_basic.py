"""
Basic tests to validate the backend functionality
"""
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.user import UserCreate
from src.services.auth import AuthService
from src.database.session import get_session
from sqlmodel import Session


def test_api_health_check():
    """Test that the API is accessible"""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_user_registration_and_authentication():
    """Test user registration and authentication flow"""
    client = TestClient(app)

    # Register a new user
    user_data = {
        "email": "test@example.com",
        "password": "securepassword123"
    }

    response = client.post("/api/auth/register", json=user_data)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "token" in response.json()

    # Login with the registered user
    login_response = client.post("/api/auth/login", json={
        "email": "test@example.com",
        "password": "securepassword123"
    })

    assert login_response.status_code == 200
    assert login_response.json()["success"] is True
    assert "token" in login_response.json()


def test_task_operations_require_authentication():
    """Test that task operations require authentication"""
    client = TestClient(app)

    # Try to get tasks without authentication
    response = client.get("/api/tasks")
    assert response.status_code == 401

    # Try to create a task without authentication
    response = client.post("/api/tasks", json={
        "title": "Test task",
        "description": "Test description",
        "completed": False
    })
    assert response.status_code == 401


if __name__ == "__main__":
    pytest.main([__file__])