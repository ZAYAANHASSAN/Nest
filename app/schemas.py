from pydantic import BaseModel
from datetime import date
from typing import Optional

# ----------------------
# Student Schemas
# ----------------------

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    age: int
    city: str
    class_id: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    middle_name: Optional[str] = None
    age: Optional[int] = None
    city: Optional[str] = None
    class_id: Optional[int] = None

    class Config:
        orm_mode = True

class StudentOut(StudentBase):
    student_id: int

    class Config:
        orm_mode = True

# ----------------------
# Class Schemas
# ----------------------

class ClassBase(BaseModel):
    class_name: str
    description: str
    start_date: date
    end_date: date
    number_of_hours: int

class ClassCreate(ClassBase):
    pass

class ClassUpdate(BaseModel):
    class_name: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    number_of_hours: Optional[int] = None

    class Config:
        orm_mode = True

class ClassOut(ClassBase):
    class_id: int

    class Config:
        orm_mode = True
