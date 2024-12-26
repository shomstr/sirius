from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from database.db_postgresql import async_db_session, scoped_session_dependency, get_db
import secrets
import uuid
from typing import Annotated, Any
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, EmailStr

from models import Users_data

router = APIRouter()


@router.post("/register")
async def register(db: AsyncSession = Depends(get_db)):
    existing_user = await Users_data.get_user(db, phone=123, password='w123w')
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уж е существует'
        )

    try:
        new_user = await Users_data.create_user(db, phone=123, password='w123w', name='John Doe', login='john_doe')
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )

    return {
        "id": new_user.id
    }
@router.post("/login")
async def login(db: AsyncSession = Depends(get_db)):
    user = await Users_data.get_user(db, phone=13, password='w123w')
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Неверная почта или пароль')
    return {
         "id": user.id
    }


