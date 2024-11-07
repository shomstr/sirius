from fastapi import FastAPI
from database.db_mysql import create_table
from database.db_mysql import async_engine
from models import Base
from configuration.server import Server
from fastapi import Depends
from sqlalchemy import URL

from typing import AsyncGenerator as async_generator
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing_extensions import Annotated
from starlette.middleware.cors import CORSMiddleware
from core.conf import settings
#from core.registr import lifespan
from pydantic import BaseModel

class Transcription(BaseModel):
    text: str


def create_app(_=None) -> FastAPI:
   
   app = FastAPI(
        title='FastAPI',
        description='Fast API' 
    )
   

   app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

   
   @app.on_event("startup")
   async def startup():
      result = await create_table()
      server = Server(app)
      return server.get_app()
   
   

   return app

if __name__ == '__main__':
   import uvicorn
   uvicorn.run(create_app(), host="127.0.0.1", port=8000)