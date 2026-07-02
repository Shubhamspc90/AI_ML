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