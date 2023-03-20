from pprint import pprint

from tests.api import auth
from tests.data_provider.user import RegisteredUser
import requests
from tests.config import BASE_URL
from app.models.enums import ConditionType


#
# r_user = RegisteredUser()
# r_user.sign_in()
#
# headers = {
#     "Authorization": f"Bearer {r_user.token}"
# }


def find_release_by_barcode(barcode):
    r = requests.get(url=f"{BASE_URL}/release/by_barcode",
                     # headers=headers,
                     params={
                         "barcode": barcode
                     }
                     )

    if r.status_code in [200, 2001]:
        return r.json()[0]['id']
    else:
        print(r.status_code, r.text)


def get_release_by_id(release_id):
    r = requests.get(url=f"{BASE_URL}/release/{release_id}",
                     # headers=headers,
                     )
    if r.status_code in [200, 2001]:
        return r.json()

    else:
        print(r.status_code, r.text)


def get_release_tracks(release_id):
    r = requests.get(url=f"{BASE_URL}/release/{release_id}/tracks",
                     # headers=headers,
                     )
    if r.status_code in [200, 2001]:
        pprint(r.json(), sort_dicts=False)
        return r.json()
    else:
        print(r.status_code, r.text)


release_id = find_release_by_barcode(barcode='744861112518')

get_release_by_id(release_id)
get_release_tracks(release_id)
