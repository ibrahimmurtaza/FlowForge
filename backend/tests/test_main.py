import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client(mock_supabase):
    return TestClient(app)

def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
