import requests 
import pytest


def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    print(response.json())

def test_users_count(base_url):
    response = requests.get(f"{base_url}/users")
    users = response.json()
    assert len(users) == 10
    print(response.json())

def test_get_single_user(base_url):
    response = requests.get(f"{base_url}/users/2")
    user = response.json()
    assert user['id'] == 2
    assert 'username' in user
    print(response.json())
def test_user_created(base_url):
    new_user = {
        "name":  "Artem",
        "job": "QA Engineer" 
    }
    response = requests.post(f"{base_url}/posts", json=new_user)
    assert response.status_code == 201
def test_user_delete(base_url):
    response = requests.delete(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json() == {}
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_users(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    user = response.json()
    assert 'username' in user
    assert response.status_code == 200
    print(response.json())