# ==========================================================
# student_crud.py
#
# Database Operations
#
# NOTE:
# Is file me sirf Database related code hoga.
# Yahan koi API (@router.get/post) nahi hogi.
# ==========================================================

from sqlalchemy.orm import Session

from app import models

from app import schemas

# ==========================================================
# CREATE STUDENT
# ==========================================================

def create_student(
    db: Session,
    student: schemas.StudentCreate
):

    # Create Student Object
    new_student = models.Student(
        name=student.name,
        email=student.email,
        age=student.age
    )

    # Add Student to Database Session
    db.add(new_student)

    # Save Changes Permanently
    db.commit()

    # Reload Latest Data
    db.refresh(new_student)

    # Return Response
    return new_student

# ==========================================================
# GET ALL STUDENTS
# ==========================================================

def get_all_students(
    db: Session
):

    # Fetch all students from database
    students = db.query(models.Student).all()

    # Return all students
    return students

# ==========================================================
# GET STUDENT BY ID
# ==========================================================

def get_student_by_id(
    db: Session,
    student_id: int
):

    # Search student using ID
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    return student


# ==========================================================
# UPDATE STUDENT
# ==========================================================

def update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentCreate
):

    existing_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if existing_student is None:
        return None

    existing_student.name = student.name
    existing_student.email = student.email
    existing_student.age = student.age

    db.commit()

    db.refresh(existing_student)

    return existing_student

# ==========================================================
# DELETE STUDENT
# ==========================================================

def delete_student(
    db: Session,
    student_id: int
):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student is None:
        return False

    db.delete(student)

    db.commit()

    return True

# ==========================================================
# GET ALL STUDENTS
#
# NOTE:
# Database se saare students fetch karega.
# ==========================================================

def get_all_students(
    db: Session
):
    # Fetch all students from database
    students = db.query(models.Student).all()

    # Return all students
    return students

# ==========================================================
# GET STUDENT BY ID
# NOTE:
# Student ko ID ke basis par database se fetch karega.
# ==========================================================

def get_student_by_id(
    db: Session,
    student_id: int
):

    # Search student using ID
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    # Return student object or None
    return student


# ==========================================================
# UPDATE STUDENT
#
# NOTE:
# Database me existing student update karega.
# ==========================================================

def update_student(
    db: Session,
    student_id: int,
    student: schemas.StudentCreate
):

    # Search student
    existing_student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    # Student not found
    if existing_student is None:
        return None

    # Update values
    existing_student.name = student.name
    existing_student.email = student.email
    existing_student.age = student.age

    # Save changes
    db.commit()

    # Reload latest data
    db.refresh(existing_student)

    # Return updated object
    return existing_student


# ==========================================================
# DELETE STUDENT
#
# NOTE:
# Database se student delete karega.
# ==========================================================

def delete_student(
    db: Session,
    student_id: int
):

    # Search Student
    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    # Student Not Found
    if student is None:
        return False

    # Delete Student
    db.delete(student)

    # Save Changes
    db.commit()

    # Return Success
    return True
