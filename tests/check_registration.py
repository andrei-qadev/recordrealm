import requests
from tests.utils import clear_all

clear_all()

BASE_URL = 'http://127.0.0.1:8000'

from pprint import pprint
import json

import requests
from decouple import config


def register_user(user_email, user_password, user_name) -> requests.Response:
    data = {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }
    r = requests.post(url=f"{config('BASE_URL')}/register",
                      json=data)
    return r


def sign_in(user_email, user_password) -> requests.Response:
    data = {
        "email": user_email,
        "password": user_password,
    }
    r = requests.post(url=f"{config('BASE_URL')}/login",
                      json=data)
    return r


r = register_user(
    user_email='andrei@gmail.com',
    user_password='qwe',
    user_name='andrei'
)
print(r.status_code)

r = sign_in(user_email='andrei@gmail.com',
            user_password='qwe')
print(r.status_code)
