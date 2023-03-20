"""
this module is responsible for
user registration and sign in logic
"""
from passlib.context import CryptContext
from asyncpg import UniqueViolationError
from fastapi import HTTPException

from app.db import database
from app.models import User, users_table
from app.managers.auth import AuthManager

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    @staticmethod
    async def register(user_data):
        # hash provided user password
        user_data["password"] = pwd_context.hash(user_data["password"])

        try:  # add user to DB
            q = users_table.insert().values(**user_data)
            id_ = await database.execute(q)

        # check the email is not in DB
        except UniqueViolationError as ex:
            # TODO: add logging
            raise HTTPException(400, 'User with this email already exists')

        # fetch created user data from DB
        created_user: User = await database.fetch_one(users_table.select().where(users_table.c.id == id_))
        # create user access token
        token = AuthManager.encode_token(user=created_user)
        return token

    @staticmethod
    async def authenticate(user_data):
        # fetch user from db by email
        db_user: User = await database.fetch_one(users_table.select()
                                                 .where(users_table.c.email == user_data['email']))
        if not db_user:  # user with provided email was not found
            raise HTTPException(400, "Wrong email or password")
        elif not pwd_context.verify(user_data["password"], db_user.password):  # provided password hash does not match the DB hash
            raise HTTPException(400, "Wrong email or password")
        # create user access token
        token = AuthManager.encode_token(user=db_user)
        return token
