from pydantic import BaseModel
from typing import Any
from loguru import logger
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse


class ErrorResponse(BaseModel):
    """Base Model for error responses"""
    status: int
    message: Any
    
    model_config = {
        "arbitrary_types_allowed": True
    }


async def http422_error_handler(_: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = " -> ".join(str(loc) for loc in error['loc'])
        message = error['msg']
        error_detail = f"Error in field '{field}': {message}"
        errors.append(error_detail)
        logger.error(error_detail)  # Log the error details

    error_response = ErrorResponse(status=422, message=errors)
    return JSONResponse(
        status_code=422,
        message=error_response.model_dump()
    )
