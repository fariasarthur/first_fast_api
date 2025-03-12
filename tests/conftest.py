import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from first_fast_api.app import app
from first_fast_api.models import table_registry


# Metodologia DRY para evitar repetição de código
@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    # banco de dados em memória que funciona somente durante o teste
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    # Garantindo que seja reinicializado
    table_registry.metadata.drop_all(engine)
