import pytz

from fastapi import FastAPI


DEFAULT_TZ = pytz.timezone("Europe/Moscow")

app = FastAPI(
        title="FastAPI",
        description="Fast API"
    )

