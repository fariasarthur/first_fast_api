from http import HTTPStatus


def test_create_user(client):
    # Act
    response = client.post(
        '/users/',
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'test',
                'email': 'test.surname@email.com',
                'id': 1,
            }
        ]
    }
