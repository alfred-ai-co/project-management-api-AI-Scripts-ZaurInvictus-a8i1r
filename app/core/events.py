from fastapi import FastAPI
from loguru import logger
from typing import Callable
from sqlalchemy.orm import Session

from app.db_models.base import Base
from app.db_models.session import engine

def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        settings = app.state.settings
        logger.info(f"Starting [{settings.app_env.value}] Application")
        # Start up Events
        
        # Create tables
        Base.metadata.create_all(bind=engine)
        
        
    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:
    @logger.catch
    async def stop_app() -> None:
        settings = app.state.settings
        logger.info(f"Stopping [{settings.app_env.value}] application")
        # Shut down events
    return stop_app