import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from configuration.server import Server
from internal.events.startup import on_startup
from core.registr import get_start

def create_app(_=None) -> FastAPI:
    app = get_start(app=FastAPI)
    server = Server(app)
    return server.get_app()
    return app

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(create_app(), host="127.0.0.1", port=8000)