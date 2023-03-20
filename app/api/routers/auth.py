"""
user registration endpoint
"""

from fastapi import APIRouter
from app.managers.user import UserManager
from app.schemas.request.user import UserRegisterIn, UserAuthenticateIn

router = APIRouter(tags=["Authentication"])


@router.post("/register",
             status_code=201,
             summary='User registration')
async def register(user_data: UserRegisterIn):
    token = await UserManager.register(user_data.dict())
    return {"token": token}


@router.post("/authenticate",
             summary='User sign in')
async def authenticate(user_data: UserAuthenticateIn):
    token = await UserManager.authenticate(user_data.dict())
    return {"token": token}
