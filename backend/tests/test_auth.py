import pytest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import MagicMock
from jose import jwt

@pytest.fixture
def client(mock_supabase):
    return TestClient(app)

def test_me_success(client):
    token = jwt.encode({"sub": "user_id_123", "email": "test@example.com"}, "dummy", algorithm="HS256")
    response = client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_register_success(client, mock_supabase):
    # Mock successful signup
    response_mock = MagicMock()
    # Mock attributes directly
    response_mock.session.access_token = "fake_access_token"
    response_mock.session.refresh_token = "fake_refresh_token"
    response_mock.user.id = "user_id_123"
    response_mock.user.email = "test@example.com"
    mock_supabase.auth.sign_up.return_value = response_mock

    response = client.post(
        "/api/auth/register",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 201
    assert response.json()["user"]["email"] == "test@example.com"
    mock_supabase.auth.sign_up.assert_called_once()

def test_login_success(client, mock_supabase):
    # Mock successful login
    response_mock = MagicMock()
    response_mock.session.access_token = "fake_access_token"
    response_mock.session.refresh_token = "fake_refresh_token"
    response_mock.user.id = "user_id_123"
    response_mock.user.email = "test@example.com"
    mock_supabase.auth.sign_in_with_password.return_value = response_mock

    response = client.post(
        "/api/auth/login",
        json={"email": "test@example.com", "password": "password123"},
    )
    assert response.status_code == 200
    assert response.json()["user"]["email"] == "test@example.com"
    mock_supabase.auth.sign_in_with_password.assert_called_once()
