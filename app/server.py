from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from fastapi.middleware import Middleware

from api import init_sub_applications
from core.config import config


def make_middleware() -> list[Middleware]:
    middleware = [
        Middleware(CorrelationIdMiddleware, header_name="X-Request-ID", validator=None),
    ]
    return middleware


def create_app() -> FastAPI:
    app_ = FastAPI(
        title=f"{config.MICROSERVICE_NAME}-service",
        description=f"{config.MICROSERVICE_NAME} Service API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        middleware=make_middleware(),
    )
    init_sub_applications(app_=app_)
    return app_


app = create_app()
