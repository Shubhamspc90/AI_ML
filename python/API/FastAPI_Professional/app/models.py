# ======================================================
# models.py
# Database Tables
# ======================================================
# SQLALchemy Column Types
from sqlalchemy import Column,Integer,String

# Base class from database.py
from app.database import Base

# ======================================================
# Student Model
#
# Ye class students table ko represent karti hai.
# ======================================================
class Student (Base):
    # Table Name in MySQL
    __tablename__="students"
    
    # Primary Key
    id = Column(Integer,primary_key=True,index=True)
    # Student Name
    name = Column( String(100),nullable=False)
    #Student Email
    email=Column(String(100),unique=True,nullable=False)
    # Student Age
    age = Column(Integer,nullable=False)
    
    