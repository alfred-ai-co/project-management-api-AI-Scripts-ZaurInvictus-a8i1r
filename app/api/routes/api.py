from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes import projects

router = APIRouter()

router.include_router(ping.router, prefix="/ping", tags=["ping"])
router.include_router(projects.router, prefix="/projects", tags=["projects"])
