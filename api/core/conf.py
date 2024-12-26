from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)

    # Env Config
    ENVIRONMENT: Literal['dev', 'pro']
    PostgreSql_HOST: str
    PostgreSql_PORT: int
    PostgreSql_USER: str
    PostgreSql_PASSWORD: str
    PostgreSql_DATABASE: str
    PostgreSql_CHARSET: str
    PostgreSql_ECHO: bool = True
    LOG_STDOUT_FILENAME: str = 'fsm_access.log'
    LOG_STDERR_FILENAME: str = 'fsm_error.log'

    #REDIS_HOST: str
    #REDIS_PORT: int


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
