# ==========================================================
# student_service.py
#
# Business Logic
# NOTE:
# Yahan sirf Business Logic hoga.
# Database query yahan nahi hogi.
# ==========================================================

from sqlalchemy.orm import Session

from app import schemas
from app.crud import student_crud

# ==========================================================
# CREATE STUDENT
#
# Business Logic
# ==========================================================

def create_student(
    db: Session,
    student: schemas.StudentCreate
):

    # Future Business Logic

    # Example:
    # Send Email
    # Generate Roll Number
    # Write Logs

    # Call CRUD Layer

    return student_crud.create_student(
        db,
        student
    )
    
# ==========================================================
# GET ALL STUDENTS
#
# Business Logic
# ==========================================================

def get_all_students(
    db: Session
):

    # Future Business Logic

    # Example:
    # Cache
    # Logs
    # Analytics

    return student_crud.get_all_students(
        db
    )
    
    
# ==========================================================
# GET STUDENT BY ID
#
# Business Logic
# ==========================================================

def get_student_by_id(
    db: Session,
    student_id: int
):

    return student_crud.get_student_by_id(
        db,
        student_id
    )
    
    
# ==========================================================
# UPDATE STUDENT
#
# Business Logic
# ==========================================================

def update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentCreate
):

    return student_crud.update_student(
        db,
        student_id,
        student
    )
    
# ==========================================================
# DELETE STUDENT
#
# Business Logic
# ==========================================================

def delete_student(
    db: Session,
    student_id: int
):

    return student_crud.delete_student(
        db,
        student_id
    )