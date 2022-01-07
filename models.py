from datetime import date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date

from database import Base

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    priority = Column(String(10))
    deadline_time = Column(Date, default=date.today)
    is_complete = Column(Boolean, default=False)
