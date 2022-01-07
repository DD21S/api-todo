from fastapi import FastAPI

from routes import routes_tasks
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes_tasks)