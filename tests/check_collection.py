from pprint import pprint

from tests.api import auth
from tests.data_provider.user import RegisteredUser
import requests
from tests.config import BASE_URL
from app.models.enums import ConditionType

r_user = RegisteredUser()
r_user.sign_in()

headers = {
    "Authorization": f"Bearer {r_user.token}"
}

list_user_releases = [
    {
        "release_id": 1,
    },
    {
        "release_id": 2,
    }
]


def add_release(payload):
    r = requests.post(url=f"{BASE_URL}/collection",
                      headers=headers,
                      json=payload
                      )

    print(r.status_code)
    # pprint(r.json())


for payload in list_user_releases:
    add_release(payload)


def get_releases():
    r = requests.get(url=f"{BASE_URL}/collection",
                     headers=headers)
    print(r.status_code)
    pprint(r.json())


get_releases()
