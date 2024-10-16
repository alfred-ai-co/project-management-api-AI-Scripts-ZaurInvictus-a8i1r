# Project Endpoints
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

import app.db_models.crud as crud
from app.api_models.projects import ProjectCreate, ProjectResponse
from app.api.dependencies.sqldb import get_db


router = APIRouter()


@router.post('', response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.create_project(db, project.name, project.description)
    return db_project

@router.get('/{project_id}', response_model=ProjectResponse)
async def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    return db_project

@router.put('/{project_id}', response_model=ProjectResponse)
async def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud.update_project(db, project_id, project.name, project.description)
    return db_project

@router.delete('/{project_id}')
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    crud.delete_project(db, project_id)
    return {'message': f'Project with id {project_id} deleted'}