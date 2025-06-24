from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    age = Column(Integer)
    city = Column(String)
    class_id = Column(Integer, ForeignKey("classes.id"), nullable=True)

class Class(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    hours = Column(Integer)
    students = relationship("Student", backref="class_")