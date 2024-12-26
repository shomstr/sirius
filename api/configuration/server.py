from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.db_postgresql import create_table
from configuration.routes import __routes__
from fastapi_utils.tasks import repeat_every
from internal.events.startup import on_startup, on_loop_startup

class Server:


    __app: FastAPI


    def __init__(self, app: FastAPI):

        self.__app = app
        self.__register_routes(app)
        self.__register_events(app)

    def get_app(self) -> FastAPI:

        return self.__app
    
    @staticmethod
    def __register_events(app):

        app.on_event('startup')(on_startup)
        app.on_event('shutdown')(on_loop_startup)
        

    @staticmethod
    def __register_routes(app):
        __routes__.register_routes(app)


    
        