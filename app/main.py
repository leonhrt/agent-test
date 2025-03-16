from fastapi import APIRouter, FastAPI
from fastapi.openapi.utils import get_openapi
from typing import Dict

from api import ask, default

app = FastAPI()

def create_router() -> APIRouter:
    router = APIRouter()
    router.include_router(default.router, tags=["default"])
    router.include_router(ask.router, tags=["ask"])
    return router

def configure_openapi() -> Dict:
    try:
        openapi = get_openapi(
            title="Test Agent",
            version="test",
            openapi_version="3.0.2",
            description="Test Agent that allows sending messages to Gemini",
            routes=app.routes
        )
        
        return openapi
    except Exception:
        return {}

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router=create_router())
    app.openapi = configure_openapi
    return app

app = create_app()
