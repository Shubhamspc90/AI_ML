# ======================================================
# schemas.py
# Request & Response Validation
# ======================================================
from pydantic import BaseModel,EmailStr


# ======================================================
# Create Student Schema
#
# POST request me use hoga.
# ======================================================
class StudentCreate(BaseModel):
    name:str
    email:EmailStr
    age:int
   
    
# ======================================================
# Response Schema
#
# API se response bhejne ke liye.
# ======================================================
class StudentResponse(BaseModel):
    id:int
    name:str
    email:EmailStr
    age:int
    
    # pydratic V2 Cofigration
    model_config={
        "from_attributes":True
    }