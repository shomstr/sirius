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
from api.schemas import PointModel, Point

router = APIRouter()

from fastapi import Depends, HTTPException
# from api.database.models import Point

router = APIRouter()


@router.post("/upload/")
async def upload_stations(file: UploadFile = File(...), repo: Repositories = Depends(get_repo)):
    if file.content_type != "application/json":
        raise HTTPException(status_code=400, detail="Файл должен быть в формате JSON")

    content = await file.read()
    try:
        data = json.loads(content)# Извлекаем массив станций
        print("Получено", len(data["points"]))
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Некорректный JSON-файл")
    c = 1
    for point in data["points"]:
        try:
            p = Point(**point)
            await repo.points.create(p)
            print(c)
            c += 1

        except ValidationError:
            raise HTTPException(status_code=400, detail="Некорректный JSON-файл")

    return {"succes": "true"}

@router.get("/point/{point_id}")
async def get_point(point_id: int, repo: Repositories = Depends(get_repo)):
    point = await repo.points.get(point_id)
    if point is None:
        raise HTTPException(status_code=400, detail="Point не найден")

    return point.to_dict(relationships=True)

@router.get("/get_all_points_coordinates/")
async def get_all_points_coordinates(repo: Repositories = Depends(get_repo)):
    points = await repo.points.get_all_points_coordinates()

    return points


# @router.get("/stations/", response_model=List[station_schemas.StationBase])
# async def read_stations(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
#     stations = await stations_crud.get_stations(db, skip=skip, limit=limit)
#     return stations
#
# @router.get("/stations/{station_id}", response_model=station_schemas.StationBase)
# async def read_station(station_id: int, db: AsyncSession = Depends(get_db)):
#     db_station = await stations_crud.get_station(db, station_id=station_id)
#     if db_station is None:
#         raise HTTPException(status_code=404, detail="Станция не найдена")
#     return db_station
#
# @router.put("/stations/{station_id}", response_model=station_schemas.StationBase)
# async def update_station(station_id: int, station: stations.StationUpdate, db: AsyncSession = Depends(get_db)):
#     db_station = await stations_crud.update_station(db, station_id=station_id, station=station)
#     if db_station is None:
#         raise HTTPException(status_code=404, detail="station_schemas не найдена")
#     return db_station
#
# @router.delete("/stations/{station_id}", response_model=station_schemas.StationBase)
# async def delete_station(station_id: int, db: AsyncSession = Depends(get_db)):
#     db_station = await stations_crud.delete_station(db, station_id=station_id)
#     if db_station is None:
#         raise HTTPException(status_code=404, detail="Станция не найдена")
#     return db_station

