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
from api.schemas.orders import Order

router = APIRouter(prefix="/user_orders")


@router.post("/create")
async def create_order(order: Order, repo: Repositories = Depends(get_repo)) -> dict:
    user: User_data = await repo.orders.create(**order.model_dump())

    return user.to_dict()


@router.get("/get/{order_id}")
async def get_order(order_id: int, repo: Repositories = Depends(get_repo)):
    order = await repo.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=400, detail="Юзер не найден")

    return order.to_dict(relationships=True)


@router.delete("/delete")
async def delete_order(order_id: int, repo: Repositories = Depends(get_repo)):
    order: UserOrder = await repo.orders.get(order_id)
    if not order:
        return HTTPException(404, "Нет информации о юзере")

    await repo.users.delete(order)

    return {"status": "successful"}











