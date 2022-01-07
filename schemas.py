from datetime import date

from typing import Optional

from pydantic import BaseModel

class TaskModel(BaseModel):

    id: Optional[int]
    name: str
    priority: str
    deadline_time: date = date.today()
    is_complete: bool = False

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Buy potato",
                "priority": "Low",
                "deadline_time": date.today(),
                "is_complete": False
            }
        }
