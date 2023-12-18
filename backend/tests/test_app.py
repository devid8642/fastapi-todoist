def test_root_returned_200_and_hello_world(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/create/',
        json={
            'username': 'devid',
            'email': 'devid@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'devid',
        'email': 'devid@example.com',
    }
