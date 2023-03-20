"""
this module is responsible for
user authorization logic
"""

from datetime import datetime, timedelta
from typing import Optional

import jwt
from decouple import config
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from app.models import User, users_table
from app.db import database
from app.models.enums import RoleType

AUTH_TOKEN_TTL = timedelta(days=30)


class AuthManager:
    @staticmethod
    def encode_token(user):
        """
        creates jwt encoded token for user authorization
        """
        try:
            payload = {"sub": user["id"],
                       "exp": datetime.utcnow() + AUTH_TOKEN_TTL}
            return jwt.encode(payload=payload,
                              key=config("JWT_SECRET"),
                              algorithm="HS256")
        except Exception as ex:
            # TODO: log the exception
            raise ex


class CustomHTTPBearer(HTTPBearer):
    """
    used in the incoming requests to check the validity of
    the provided user auth token
    """

    async def __call__(
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        response = await super().__call__(request)
        try:
            payload = jwt.decode(response.credentials,
                                 config("JWT_SECRET"),
                                 algorithms=["HS256"])  # decodes jwt payload from token
            user = await database.fetch_one(users_table
                                            .select()
                                            .where(users_table.c.id == payload["sub"]))  # fetch user by ID retrieved from token's payload
            request.state.user = user  # binds globally user to the requests by its JWT
            return user
        except jwt.ExpiredSignatureError:  # if token expired
            raise HTTPException(401, "Token is expired")
        except jwt.InvalidTokenError:  # if token invalid
            raise HTTPException(401, "Invalid token")


oauth2_scheme = CustomHTTPBearer()


def is_user(request: Request):
    if not request.state.user["role"] == RoleType.user:
        raise HTTPException(403, "Forbidden")
