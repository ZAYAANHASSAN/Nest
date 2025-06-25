from fastapi import FastAPI
from . import models
from .database import engine
from .routes import student_routes, class_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_routes.router)
app.include_router(class_routes.router)

