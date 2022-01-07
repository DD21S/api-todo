from fastapi import HTTPException, status

from sqlalchemy.orm import Session

import models, schemas

task_not_exist_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="This task does not exist"
)

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    db_task = db.query(models.Task).get(task_id)

    if db_task:
        return db_task

    raise task_not_exist_exception

def create_task(db: Session, task: schemas.TaskModel):
    db_task = models.Task(
        name=task.name,
        priority=task.priority,
        deadline_time=task.deadline_time,
        is_complete=task.is_complete
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def update_task(db: Session, task_id: int, task: schemas.TaskModel):
    db_task = db.query(models.Task).get(task_id)

    try:
        db_task.name = task.name
        db_task.priority = task.priority
        db_task.deadline_time = task.deadline_time
    except:
        raise task_not_exist_exception

    db.commit()

    return db_task

def update_status_task(db: Session, task_id: int):
    db_task = db.query(models.Task).get(task_id)

    try:
        if db_task.is_complete:
            db_task.is_complete = False
        else:
            db_task.is_complete = True
    except:
        raise task_not_exist_exception
    
    db.commit()

    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).get(task_id)

    try:
        db.delete(db_task)
    except:
        raise task_not_exist_exception
    
    db.commit()

    return db_task