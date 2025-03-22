from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import secrets
import uuid
import json
from typing import Annotated, Any, List
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.database import get_repo, Repositories
from api.database.models import User_data, UserOrder
from api.schemas.auth import Registration


router = APIRouter(prefix="/user")

@router.post("/create")
async def create_user(reg: Registration, repo: Repositories = Depends(get_repo)) -> dict:
    user: User_data = await repo.users.create(**reg.model_dump())

    return user.to_dict()


@router.get("/get/{user_id}")
async def get_user(user_id: int, repo: Repositories = Depends(get_repo)):
    user: User_data = await repo.users.get(user_id, User_data.orders)
    if user is None:
        raise HTTPException(status_code=400, detail="Юзер не найден")

    return user.to_dict(relationships=True)


@router.delete("/delete")
async def delete_user(user_id: int, repo: Repositories = Depends(get_repo)):
    user: User_data = await repo.users.get(user_id)
    if not user:
        return HTTPException(404, "Нет информации о юзере")

    await repo.users.delete(user)

    return {"status": "successful"}











