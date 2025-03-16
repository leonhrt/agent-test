from fastapi import APIRouter

from schemas.default import HealthCheck

router = APIRouter()

@router.get("/")
async def root() -> str:
    return "TEST"

@router.get("/health")
async def health() -> HealthCheck:
    return HealthCheck(status="OK")
