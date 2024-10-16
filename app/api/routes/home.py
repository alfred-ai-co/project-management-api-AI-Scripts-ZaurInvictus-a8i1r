from fastapi import APIRouter


router = APIRouter()


@router.get("/", status_code=200)
async def home():
    return "Welcome to the FastAPI Application for Alfred AI"


@router.get("/health", status_code=200)
async def health():
    return "OK"
