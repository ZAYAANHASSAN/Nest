# app/main.py
from fastapi import FastAPI
from app.routes import student_routes, class_routes
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_routes.router, prefix="/students")
app.include_router(class_routes.router)
