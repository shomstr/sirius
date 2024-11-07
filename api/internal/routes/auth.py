from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_mysql import async_db_session, scoped_session_dependency, get_db
import secrets
import uuid
from typing import Annotated, Any
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, EmailStr

from models import User

router = APIRouter()

class Login(BaseModel):
    email: EmailStr
    password: str

class Register(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(user: Register, db: AsyncSession = Depends(get_db)):
    try:
        user = await User.create_user(db, user.email, user.password)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    return {
        "id": user.id
    }

@router.post("/login")
async def login(user: Login, db: AsyncSession = Depends(get_db)):
    user = await User.get_user(db, user.email, user.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    return {
         "id": user.id
    }


