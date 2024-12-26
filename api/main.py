import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from configuration.server import Server
from internal.events.startup import on_startup

# Настройка логирования
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

logger = logging.getLogger(__name__)

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

    server = Server(app)
    return server.get_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(create_app(), host="127.0.0.1", port=8000)