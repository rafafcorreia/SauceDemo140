import requests
import json

url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

pet_id = 1237214124
pet_name = 'Pipoca'
pet_tag_id = 1
pet_tag_name = 'vacinado'

def test_post_pet():
     
    pet=open('./fixtures/json/pet1.json')
    data=json.loads(pet.read())

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['tags'][0]['name'] == pet_tag_name



def test_get_pet():

    response = requests.get(
        url=url + f'/{pet_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['tags'][0]['name'] == pet_tag_name

def test_put_pet():
    pet=open('./fixtures/json/pet2.json')
    data=json.loads(pet.read())

    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['status'] == 'indisponivel'

def test_delete_pet():

    response = requests.delete(
        url=url + f'/{pet_id}',
        headers=headers,
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)
