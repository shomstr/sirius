from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
import logging
from core.conf import settings
from database.db_postgresql import create_table
from database.db_postgresql import async_engine
from models import Base
from configuration.server import Server
from middleware.access_middle import AccessMiddleware

logger = logging.getLogger(__name__)

def logs():
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
    )

# Установка уровня логирования для SQLAlchemy
    logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)