import string
import pytest
import requests
import random

# print(response.json())
# json_content = response.json()
# print(response.status.code)
# print(response.text)
# text_content = response.text
# binary_content = response.content
# response = requests.get('https://reqres.in/api/users/2', timeout=5)

# registration new user


@pytest.mark.user_registration
def test_user_registration(api_url, faker_data):
    user_data = {
        "username": faker_data.user_name(),
        "email": faker_data.email(),
        "password": faker_data.password()
    }
    response = requests.post(f"{api_url}/users/", json=user_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["username"] == user_data["username"]
    assert response.json()["email"] == user_data["email"]
