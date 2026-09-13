import os
import pytest
from unittest.mock import MagicMock
from app.supabase_client import get_supabase_client

# Set environment variables for config loading
os.environ["SUPABASE_URL"] = "http://localhost:54321"
os.environ["SUPABASE_ANON_KEY"] = "dummy"
os.environ["SUPABASE_JWT_SECRET"] = "dummy"

from app.main import app

@pytest.fixture
def mock_supabase():
    mock = MagicMock()
    app.dependency_overrides[get_supabase_client] = lambda: mock
    return mock
