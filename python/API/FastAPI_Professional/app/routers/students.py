# FastAPI Imports
from fastapi import APIRouter,Depends,status,HTTPException

# SQLAlchemy Session
from sqlalchemy.orm import Session

# Import Database Dependency
from app.database import get_db

# Import Schemas
from app import schemas

# Router Object
router = APIRouter( prefix="/students", tags=["Students"] )

from app.services import student_service

# CREATE STUDENT API
@router.post("/",response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED )
def create_student(
    student:schemas.StudentCreate,
    db:Session = Depends(get_db)
):  
    # Call  service function
    return student_service.create_student(
    db,
    student
)
    


# GET ALL STUDENTS
@router.get("/",response_model=list[schemas.StudentResponse],status_code=status.HTTP_200_OK)
def get_all_students(
    db: Session = Depends(get_db)
):
    return student_service.get_all_students(db)


# GET STUDENT BY ID
@router.get("/{student_id}", response_model=schemas.StudentResponse,status_code=status.HTTP_200_OK)
def get_student_by_id(
    student_id:int,
    db:Session = Depends(get_db)
): 
    # Call CRUD Function
    student = student_service.get_student_by_id(
        db,
        student_id
    )

    if student is None:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return student
    


# UPDATE STUDENT API

@router.put("/{student_id}",response_model=schemas.StudentResponse, status_code=status.HTTP_200_OK)
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    # Call CRUD Function
    updated_student = student_service.update_student(
        db,
        student_id,
        student
    )

    if updated_student is None:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return updated_student


# DELETE STUDENT API
@router.delete("/{student_id}",status_code=status.HTTP_200_OK)
def delete_student(student_id:int , db:Session=Depends(get_db)):
    deleted = student_service.delete_student(
        db,
        student_id
    )

    if deleted is False:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

    return {
        "message": "Student Deleted Successfully"
    }