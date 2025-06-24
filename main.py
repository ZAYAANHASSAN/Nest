from fastapi import FastAPI
from app.routes import student_routes, class_routes

app = FastAPI()

app.include_router(student_routes.router, prefix="/students", tags=["Students"])
app.include_router(class_routes.router, prefix="/classes", tags=["Classes"])