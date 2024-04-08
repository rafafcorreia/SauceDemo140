import requests
import json

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

user_id = 1234567890804
username = 'fulanoCiclano'
user_firstName = 'Fulano'
user_lastName = 'Ciclano'
user_password = 'senha123'
token = ''

def test_post_user():
     
    user=open('./fixtures/json/user1.json')
    data=json.loads(user.read())

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)

def test_login():

    params = {'username': username, 'password': user_password}

    response = requests.get(
        url=url + '/login',
        headers=headers,
        params=params
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    message = response_body['message']
    token = message.removeprefix('logged in user session:')
    print('\nMensagem: ' + message)
    print('Token: ' + token)

def test_get_user():

    response = requests.get(
        url=url + f'/{username}',
        headers=headers,
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == user_id
    assert response_body['username'] == username
    assert response_body['firstName'] == user_firstName
    assert response_body['lastName'] == user_lastName
    assert response_body['password'] == user_password

def test_put_user():
    user=open('./fixtures/json/user2.json')
    data=json.loads(user.read())

    response = requests.put(
        url=f'{url}/{username}',
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)

def test_delete_user():

    response = requests.delete(
        url=url + f'/{username}',
        headers=headers,
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == username
