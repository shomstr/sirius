from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Station
from typing import List, Optional
from models.schemas.stations import StationBase

class StationsCRUD:
    async def create_station(self, db: AsyncSession, station: StationBase) -> Station:
        """
        Создать новую станцию.
        :param db: Асинхронная сессия SQLAlchemy.
        :param station: Данные для создания станции.
        :return: Созданная станция.
        """
        db_station = Station(**station.dict())
        db.add(db_station)
        await db.commit()
        await db.refresh(db_station)
        return db_station

    async def get_stations(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Station]:
        """
        Получить список станций с пагинацией.
        :param db: Асинхронная сессия SQLAlchemy.
        :param skip: Количество записей для пропуска.
        :param limit: Максимальное количество записей для возврата.
        :return: Список станций.
        """
        result = await db.execute(select(Station).offset(skip).limit(limit))
        stations = result.scalars().all()
        return stations

    async def get_station(self, db: AsyncSession, station_id: int) -> Optional[Station]:
        """
        Получить станцию по ID.
        :param db: Асинхронная сессия SQLAlchemy.
        :param station_id: ID станции.
        :return: Станция или None, если не найдена.
        """
        result = await db.execute(select(Station).filter(Station.id == station_id))
        station = result.scalars().first()
        return station

    async def update_station(self, db: AsyncSession, station_id: int, station: StationBase) -> Optional[Station]:
        """
        Обновить данные станции.
        :param db: Асинхронная сессия SQLAlchemy.
        :param station_id: ID станции.
        :param station: Новые данные для станции.
        :return: Обновленная станция или None, если не найдена.
        """
        db_station = await self.get_station(db, station_id)
        if db_station:
            for key, value in station.dict().items():
                setattr(db_station, key, value)
            await db.commit()
            await db.refresh(db_station)
        return db_station

    async def delete_station(self, db: AsyncSession, station_id: int) -> Optional[Station]:
        """
        Удалить станцию по ID.
        :param db: Асинхронная сессия SQLAlchemy.
        :param station_id: ID станции.
        :return: Удаленная станция или None, если не найдена.
        """
        db_station = await self.get_station(db, station_id)
        if db_station:
            await db.delete(db_station)
            await db.commit()
        return db_station