from fastapi import APIRouter, Depends, status

from typing import List

from sqlalchemy.orm import Session

from database import SessionLocal, engine
import crud, schemas

routes_tasks = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@routes_tasks.get(
    "/",
    response_model=List[schemas.TaskModel],
    status_code=status.HTTP_200_OK
)
async def all_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)

    return tasks

@routes_tasks.get(
    "/{task_id}",
    response_model=schemas.TaskModel,
    status_code=status.HTTP_200_OK
)
async def task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id=task_id)

    return task

@routes_tasks.post(
    "/",
    response_model=schemas.TaskModel,
    status_code=status.HTTP_201_CREATED
)
async def create_task(task: schemas.TaskModel, db: Session = Depends(get_db)):
    task = crud.create_task(db, task=task)

    return task

@routes_tasks.put(
    "/{task_id}",
    response_model=schemas.TaskModel,
    status_code=status.HTTP_200_OK
)
async def update_task(
    task_id: int,
    task: schemas.TaskModel,
    db: Session = Depends(get_db)
):
    task = crud.update_task(db,  task_id=task_id, task=task)

    return task

@routes_tasks.patch(
    "/{task_id}",
    response_model=schemas.TaskModel,
    status_code=status.HTTP_200_OK
)
async def change_status_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.update_status_task(db, task_id=task_id)

    return task

@routes_tasks.delete(
    "/{task_id}",
    response_model=schemas.TaskModel,
    status_code=status.HTTP_200_OK
)
async def drop_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, task_id=task_id)

    return task