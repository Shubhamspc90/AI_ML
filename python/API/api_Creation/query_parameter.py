from fastapi import FastAPI
app=FastAPI()

# Single Query Parameter
@app.get("/student")
def get_student(id:int):
    return{
        "student ID": id
    }
# http://127.0.0.1:8000/student?id=10

# Multiple Query Parameters
@app.get("/teacher")
def teacher(id: int, name: str):
    return {
        "Teacher ID": id,
        "Teacher Name": name
    }
# http://127.0.0.1:8000/teacher?id=101&name=Shubham

# Default Value
@app.get("/employee")
def employee(name: str = "Unknown"):
    return {
        "Employee": name
    }
# Without Query Parameter  => # http://127.0.0.1:8000/employee  
#With Query Parameter      => # http://127.0.0.1:8000/employee?name=Shubham
 

# Path + Query Parameter
@app.get("/college/{college_id}")
def college(college_id: int, city: str):
    return {
        "College ID": college_id,
        "City": city
    }
# http://127.0.0.1:8000/student/101?city=Delhi   
    
   
# Multiple Query Parameters
@app.get("/employee")
def employee(name: str, age: int, city: str):
    return {
        "Name": name,
        "Age": age,
        "City": city
    }
# http://127.0.0.1:8000/employee?name=Shubham&age=22&city=Delhi
