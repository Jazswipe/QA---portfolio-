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
def test_user_created():
    new_user = {
        "name":  "Artem",
        "job": "QA Engineer" 
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_user)
    assert response.status_code == 201
def test_user_delete():
    response = requests.delete(f"{BASE_URL}/users/1")
    assert response.status_code == 200