from fastapi import FastAPI , Query
from typing import Optional  # for Optional Query Parameter
app=FastAPI()

@app.get("/student")
def student(name:str = Query()):
    return{
        "student":name
    }
    
    
# Minimum Length
@app.get("/teacher")
def get_teacher(name:str = Query(min_length=3)):
    return{
        "name":name
    }
    
@app.get("/college")
def get_collage(name:str=Query(min_length=3,max_length=10)):
    return{
        "name":name
    }
    
# Number Validation
# if  gt=18  => greater than 18 (19,20,21,... allow ),18 not allow
@app.get("/age")
def get_age(Age : int=Query(gt=18)):
    return{
        "Age":Age
    }
# if  ge=18  => greater than or equal to 18 (18,19,20,21,... allow )
@app.get("/balance")
def balance(my_balance : int=Query(gt=18)):
    return{
        "My Age":my_balance
    }


   
# if  lt=100 => samller than 100(99,98,97,... allow) 
@app.get("/salary")
def salary(my_salary:float=Query(lt=100)):
    return{
        "salray":my_salary
    }
    
# if  le=100 => samller than or equal to 100(100,99,98,97,... allow) 
@app.get("/mark")
def get_mark(marks:float=Query(le=100)):
    return{
        "Marks":marks
    }

#Combine Validation
@app.get("/doctor")
def  get_doctor(
    name:str=Query(min_length=4,max_length=30),age:int=Query(ge=25,le=50)):
    return{
       "Doctor name" : name,
       "Age": age
    }
    
# Description
@app.get("/city")
def city(city:str=Query(description="Enter city name")):
    return {
        "City": city
    }
  
# Default Value
@app.get("/food")
def get_food(
    food: str = Query(default="Pizza")
):
    return {
        "Food": food
    }
    

# Optional Query Parameter
# old method 
@app.get("/subject")
def get_student(sub: Optional[str] = Query(default=None)):
    return {
        "Subject": sub
    }
    
# new method 
@app.get("/employee")
def employee(
    name: str | None = Query(default=None),
    age: int | None = Query(default=None)
):
    return {
        "Name": name,
        "Age": age
    }