from http import HTTPStatus

from fastapi.testclient import TestClient

from first_fast_api.app import app


def test_read_root_return_ok_and_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'olá, tabacudo'}  # Assert


def test_read_HTML_return_ok_and_text():
    client = TestClient(app)  # Arrange

    response = client.get('/secundario')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert '<h1>SOY ASI UN TABACUDO</h1>' in response.text  # Assert
