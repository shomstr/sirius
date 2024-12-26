import sys
from uuid import uuid5
from models import Base

from fastapi import Depends
from sqlalchemy import URL
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)


from common.log import log
from core.conf import settings


def create_engine_and_session(url: str | URL):
    try:
        engine = create_async_engine(url, echo=settings.PostgreSql_ECHO, future=True, pool_pre_ping=True)
        log.success('successfully created engine')
    except Exception as e:
        log.error('error {}', e)
        sys.exit()
    else:
        db_session = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False, autocommit=False)
        return engine, db_session


SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{settings.PostgreSql_USER}:{settings.PostgreSql_PASSWORD}@{settings.PostgreSql_HOST}:'
    f'{settings.PostgreSql_PORT}/{settings.PostgreSql_DATABASE}'
)


async_engine, async_db_session = create_engine_and_session(SQLALCHEMY_DATABASE_URL)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session = async_db_session()
    try:
        yield session
    except Exception as se:
        await session.rollback()
        raise se
    finally:
        await session.close()


CurrentSession = Annotated[AsyncSession, Depends(get_db)]


async def create_table():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
async def scoped_session_dependency(self) -> AsyncSession:
    session = self.get_scoped_session()
    yield session
    await session.close()



def uuid4_str() -> str:
    return str(uuid5())