from fastapi import FastAPI, Depends , HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, Base, get_db

app = FastAPI()

# Create Tables
Base.metadata.create_all(bind=engine)


# ===========================
# Home API,  http://127.0.0.1:8000/  ,, No body needed
# ===========================

@app.get("/")
def home():
    return {
        "message": "FastAPI + MySQL Connected Successfully"
    }


# ===========================
# CREATE Student  ,, http://127.0.0.1:8000/students ,,with json data in body section
# ===========================

# @app.post("/students")
@app.post("/students", response_model=schemas.StudentCreateResponse)
def create_student(student: schemas.StudentCreate,
                   db: Session = Depends(get_db)):

    existing_student = db.query(models.Student).filter(
        models.Student.email == student.email
    ).first()

    if existing_student:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_student = models.Student(
        name=student.name,
        email=student.email,
        age=student.age
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student Added Successfully",
        "student": new_student
    }


# ===========================
# READ All Students  ,, http://127.0.0.1:8000/students  , No body  needed
# ===========================

@app.get("/students", response_model=list[schemas.StudentResponse])
def get_all_students(db: Session = Depends(get_db)):

    students = db.query(models.Student).all()

    return students


# ===========================
# READ Student By ID  ,, http://127.0.0.1:8000/students/4  ,No body needed
# ===========================

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student_by_id(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    if student is None:    # GET BY ID Error Handling

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    return student


# ===========================
# UPDATE Student  ,, http://127.0.0.1:8000/students/4   with json data in body
# ===========================

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    updated_student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
        
    student.name = updated_student.name
    student.email = updated_student.email
    student.age = updated_student.age

    db.commit()
    db.refresh(student)
    return student

# ===========================
# DELETE Student  ,,  http://127.0.0.1:8000/students/4  ,  No body
# ===========================
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()
    
    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
        
    db.delete(student)
    db.commit()
    return {
        "message": "Student Deleted Successfully"
    }