import uuid
from dataclasses import dataclass, field
from app.models.enums import RoleType
from pprint import pprint

from faker import Faker

from tests.api import auth
from tests.utils.db import fetch_user_data_by_id

fake = Faker()


@dataclass
class BaseUser:
    id: str = field(init=False)
    email: str = f"testqacf+{uuid.uuid4()}@gmail.com"
    name: str = fake.name()
    role: RoleType = RoleType.user
    password: str = "qwerty"
    token: str = field(init=False)


@dataclass
class UnregisteredUser(BaseUser):
    def __init__(self):
        super().__init__()


@dataclass
class RegisteredUser(BaseUser):
    def __post_init__(self) -> None:
        r = auth.register_user(user_email=self.email,
                               user_password=self.password,
                               user_name=self.name)

        self.token = r.json()['token']

    def sign_in(self) -> None:
        r = auth.sign_in(user_email=self.email,
                         user_password=self.password)
        self.token = r.json()['token']


@dataclass
class DBUser:
    id: str
    email: str = field(init=False)
    name: str = field(init=False)
    role: str = field(init=False)
    password: str = field(init=False, repr=False)

    def __post_init__(self):
        user_db_data = fetch_user_data_by_id(user_id=self.id)
        self.email = user_db_data["email"]
        self.name = user_db_data["name"]
        self.role = user_db_data["role"]
        self.password = user_db_data["password"]


if __name__ == "__main__":
    # u_user = UnregisteredUser()
    # pprint(u_user)
    r_user = RegisteredUser()
    r_user.sign_in()
    pprint(r_user)
    db_user = DBUser(id=r_user.id)
    pprint(db_user)
    assert r_user.role == db_user.role
