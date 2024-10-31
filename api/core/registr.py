from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_limiter import FastAPILimiter
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from core.conf import settings
from database.db_mysql import create_table
from middleware.access_middle import AccessMiddleware


def register_middleware(app) -> None:
    
    if settings.MIDDLEWARE_GZIP:
        app.add_middleware(GZipMiddleware)
    if settings.MIDDLEWARE_ACCESS:
        app.add_middleware(AccessMiddleware)
    
    if settings.MIDDLEWARE_CORS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


