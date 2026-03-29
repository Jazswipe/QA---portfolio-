import requests 


BASE_URL = "https://jsonplaceholder.typicode.com"

def test_ger_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    print(response.json())

def test_users_count():
    response = requests.get(f"{BASE_URL}/users")
    users = response.json()
    assert len(users) == 10
    print(response.json())

def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2")
    user = response.json()
    assert user['id'] == 2
    assert 'username' in user
    print(response.json())