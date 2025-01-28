from http import HTTPStatus


def test_create_user(client):
    # Act
    response = client.post(
        '/users',
        json={
            'username': 'test',
            'email': 'test.surname@email.com',
            'password': 'test123',
        },
    )

    # Assert
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'test',
        'email': 'test.surname@email.com',
        'id': 1,
    }
