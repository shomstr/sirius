import os
import logging
from fastapi import FastAPI
from database.db_postgresql import create_table
from database.db_postgresql import async_engine
from models import Base
from fastapi import Depends
from sqlalchemy import URL
from typing import AsyncGenerator as async_generator
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing_extensions import Annotated

import aiohttp

async def on_startup():

    await create_table()
    print('Успешно запущено')

async def on_loop_startup():
    print('Остановка')