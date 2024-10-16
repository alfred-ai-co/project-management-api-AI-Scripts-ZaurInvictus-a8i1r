from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectResponse(ProjectCreate):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

