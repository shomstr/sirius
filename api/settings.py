from __future__ import annotations

from pathlib import Path
from typing import Literal

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from redis.asyncio import Redis

from api.enums.db import Databases, PostgreSQLDrivers, MySQLDrivers

load_dotenv(find_dotenv())

ProjectDir = Path(__file__).parent.parent
Api_Dir = ProjectDir / "api"
LogDir = Path(ProjectDir) / "logs"



class DatabaseSettings(BaseSettings):
    used: Databases = Databases.PostgreSQl
    ip: str
    user: str
    password: str
    name: str

    test_name: str | None = None

    model_config = SettingsConfigDict(env_prefix="DB_")

    def build_postgres_url(
            self,
    ) -> str:
        return f"postgresql+{PostgreSQLDrivers.ASYNC_DRIVER}://" f"{self.user}:{self.password}" f"@{self.ip}/{self.name}"

    def build_mysql_url(
            self,
    ) -> str:
        return f"mysql+{MySQLDrivers.ASYNC_DRIVER}://" f"{self.user}:{self.password}" f"@{self.ip}/{self.name}"


class RedisSettings(BaseSettings):
    use: bool
    ip: str
    port: int
    password: str

    model_config = SettingsConfigDict(env_prefix="REDIS_")

    def get_redis(self, db: int = 0) -> Redis:
        return Redis(host=self.ip, port=self.port, password=self.password, db=db)


class Settings(BaseSettings):
    db: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()


settings = Settings()
