# Ye API Request aur Response define karta hai.
from pydantic import BaseModel, EmailStr,ConfigDict


class StudentCreate(BaseModel):

    name: str
    email: EmailStr
    age: int
    
    
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    model_config = ConfigDict(from_attributes=True)
    
class StudentCreateResponse(BaseModel):
    message: str
    student: StudentResponse