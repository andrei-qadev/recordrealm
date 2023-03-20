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


def find_artist(substring):
    r = requests.get(url=f"{BASE_URL}/artist/{substring}",
                     headers=headers)
    print(r.status_code)
    pprint(r.json(), sort_dicts=False)


find_artist('jorja smith')

#
# def get_artist_release_groups(artist_id):
#     r = requests.get(url=f"{BASE_URL}/artist/{artist_id}/release_groups",
#                      headers=headers)
#     print(r.status_code)
#     pprint(r.json(), sort_dicts=False)
#
#
# artist_id = 191456789
# get_artist_release_groups(artist_id)
