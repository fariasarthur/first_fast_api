import pytest
from fastapi.testclient import TestClient

from first_fast_api.app import app


# Metodologia DRY para evitar repetição de código
@pytest.fixture
def client():
    return TestClient(app)
