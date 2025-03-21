from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

import secrets
import uuid
import json
from typing import Annotated, Any, List
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, EmailStr, ValidationError

from api.database import get_repo, Repositories
from api.database.models import CarWash
from api.schemas import PointModel, Point

router = APIRouter()

from fastapi import Depends, HTTPException
# from api.database.models import Point

router = APIRouter(prefix="/car_wash")


@router.post("/add_car")
async def add_car(car_id: int, repo: Repositories = Depends(get_repo)):
    car_wash: CarWash = await repo.wash.create(car_id=car_id)

    return car_wash.to_dict()


@router.post("/get_car_info")
async def get_car_info(car_id: int, repo: Repositories = Depends(get_repo)):
    car_wash: CarWash = await repo.wash.get_car(car_id)
    if not car_wash:
        return HTTPException(404, "Нет информации о машине")

    return car_wash.to_dict()


@router.delete("/delete_car")
async def delete_car(car_id: int, repo: Repositories = Depends(get_repo)):
    car_wash: CarWash = await repo.wash.get_car(car_id)
    if not car_wash:
        return HTTPException(404, "Нет информации о машине")

    await repo.wash.delete(car_wash)

    return {"status": "successful"}


@router.post("/set_temperature")
async def set_temperature(car_id: int, temperature: int, repo: Repositories = Depends(get_repo)):
    car_wash: CarWash = await repo.wash.get_car(car_id)
    if not car_wash:
        return HTTPException(404, "Нет информации о машине")

    car_wash.temperature = temperature
    await repo.wash.update(car_wash)

    return {"status": "successful"}


@router.post("/set_status")
async def set_status(car_id: int, status: bool, repo: Repositories = Depends(get_repo)):
    car_wash: CarWash = await repo.wash.get_car(car_id)
    if not car_wash:
        return HTTPException(404, "Нет информации о машине")

    car_wash.started = status
    await repo.wash.update(car_wash)

    return {"status": "successful"}





