from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession


from database.db_postgresql import async_db_session, scoped_session_dependency, get_db
import secrets
import uuid
import json
from typing import Annotated, Any, List
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel, EmailStr
from models.schemas import stations
from models.stations import Station 
from database.crud.stations_crud import StationsCRUD

from models import Users_data

router = APIRouter()

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db_postgresql import get_db
from database.crud.stations_crud import StationsCRUD
from models.schemas import stations as station_schemas

router = APIRouter()

# Создаем экземпляр CRUD-класса
stations_crud = StationsCRUD()

@router.post("/upload/", response_model=List[station_schemas.StationBase])
async def upload_stations(file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    if file.content_type != "application/json":
        raise HTTPException(status_code=400, detail="Файл должен быть в формате JSON")

    content = await file.read()
    try:
        data = json.loads(content)
        stations_data = data.get("points", [])  # Извлекаем массив станций
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Некорректный JSON-файл")

    if not isinstance(stations_data, list):
        raise HTTPException(status_code=400, detail="JSON должен содержать массив станций")

    for station_data in stations_data:
        station = station_schemas.StationBase(**station_data)
        await stations_crud.create_station(db, station)

    return stations_data

@router.get("/stations/", response_model=List[station_schemas.StationBase])
async def read_stations(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    stations = await stations_crud.get_stations(db, skip=skip, limit=limit)
    return stations

@router.get("/stations/{station_id}", response_model=station_schemas.StationBase)
async def read_station(station_id: int, db: AsyncSession = Depends(get_db)):
    db_station = await stations_crud.get_station(db, station_id=station_id)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Станция не найдена")
    return db_station

@router.put("/stations/{station_id}", response_model=station_schemas.StationBase)
async def update_station(station_id: int, station: stations.StationUpdate, db: AsyncSession = Depends(get_db)):
    db_station = await stations_crud.update_station(db, station_id=station_id, station=station)
    if db_station is None:
        raise HTTPException(status_code=404, detail="station_schemas не найдена")
    return db_station

@router.delete("/stations/{station_id}", response_model=station_schemas.StationBase)
async def delete_station(station_id: int, db: AsyncSession = Depends(get_db)):
    db_station = await stations_crud.delete_station(db, station_id=station_id)
    if db_station is None:
        raise HTTPException(status_code=404, detail="Станция не найдена")
    return db_station