from pydantic import BaseModel, validator
from email_validator import validate_email, EmailNotValidError


# validation with custom fields
class EmailField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, email) -> str:
        try:
            validate_email(email=email,
                           test_environment=True)  # TODO: move flag to env params
            return email  # returns email value to the model. If not present - will return None
        except EmailNotValidError:
            raise ValueError("Email is not valid")


class BaseUser(BaseModel):
    email: EmailField


# user request schema
class UserRegisterIn(BaseUser):
    password: str
    name: str


class UserAuthenticateIn(BaseUser):
    password: str
