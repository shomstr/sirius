from typing import Optional, Dict, List

from sqlalchemy import insert, select, update, delete # Импорт функций из SQLAlchemy
from sqlalchemy.ext.asyncio import AsyncSession

from models import Base
from database.db_mysql import async_db_session

class SQLAlchemyRepository:
    model = None

    async def add_one(self, data: Dict) -> int:
        async with async_db_session() as session:
            stmt = insert(self.model).values(*data).returning(self.model.id) # Теперь insert будет корректно определен
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
    
    async def find_all(self) -> List[Base]:
        async with async_db_session() as session:
            stmt = select(self.model) # select также корректно определен
            res = await session.execute(stmt)
            return [row[0] for row in res.all()]

    async def find_one(self, id: int) -> Optional[Base]:
        async with async_db_session() as session:
            stmt = select(self.model).where(self.model.id == id) # select также корректно определен
            res = await session.execute(stmt)
            return res.scalar_one_or_none()

    async def update(self, id: int, data: Dict) -> None:
        async with async_db_session() as session:
            stmt = update(self.model).where(self.model.id == id).values(*data) # update корректно определен
            await session.execute(stmt)
            await session.commit()

    async def delete(self, id: int) -> None:
        async with async_db_session() as session:
            stmt = delete(self.model).where(self.model.id == id) # delete корректно определен
            await session.execute(stmt)
            await session.commit()

    async def get_by_id(self, id: int) -> Optional[Base]:
        async with async_db_session() as session:
            stmt = select(self.model).where(self.model.id == id)
            res = await session.execute(stmt)
            return res.scalar_one_or_none()
