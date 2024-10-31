from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)

    # Env Config
    ENVIRONMENT: Literal['dev', 'pro']

    # Env MySQL
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_CHARSET: str
    MYSQL_ECHO: bool = False

    REDIS_HOST: str
    REDIS_PORT: int

    LOG_STDOUT_FILENAME: str = 'fsm_access.log'
    LOG_STDERR_FILENAME: str = 'fsm_error.log'

    CORS_ORIGINS: str



@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
