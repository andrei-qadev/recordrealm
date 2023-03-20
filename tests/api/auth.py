from pprint import pprint
import json

import requests
from tests.config import BASE_URL


def register_user(user_email, user_password, user_name) -> requests.Response:
    data = {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }
    r = requests.post(url=f"{BASE_URL}/register",
                      json=data)
    return r


def sign_in(user_email, user_password) -> requests.Response:
    data = {
        "email": user_email,
        "password": user_password,
    }
    r = requests.post(url=f"{BASE_URL}/authenticate",
                      json=data)
    return r
