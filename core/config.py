import os
from uuid import uuid4

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Конфиг для приложения, подбирает .env файл и перезаписывает переменные, если имеются такие же тут,
    """

    # APP
    ENV: str = "development"

    # # FastAPI
    MICROSERVICE_NAME: str = "remnawave-orkestrator"  # CHANGEME
    APP_HOST: str = "localhost"
    APP_PORT: int = 8889

    APP_UNIQUE_ID: str = str(uuid4().hex[:10])

    BEARER_TOKEN_FOR_API: str = "token"  # CHANGEME

    # # LOGGING
    DEBUG: bool = True

    # Databases
    # # Postgresql
    DB_NAME: str = "betronic"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_DRIVER: str = "postgresql+asyncpg"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    DATABASE_MAX_OVERFLOW: int = 15
    DATABASE_POOL_SIZE: int = 30
    DATABASE_ECHO: bool = False

    @property
    def db_url(self) -> str:
        return (
            f"{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


class DevelopmentConfig(Config):
    DATABASE_ECHO: bool = True


class ProductionConfig(Config):
    DEBUG: bool = False


def get_config() -> Config:
    env = os.getenv("ENV", "local")
    config_type = {
        "local": DevelopmentConfig(),
        "production": ProductionConfig(),
    }

    return config_type[env]


config: Config = get_config()
