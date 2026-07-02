from fastapi import FastAPI
app=FastAPI()

@app.get("/stud/{stud_id}")
def get_student(stud_id):
    return{
        "Student Id ": stud_id
    }
    
@app.get("/student/{student_id}")
def get_student(student_id:int):
    return{
        "Student ID": student_id,
        "type":str(type(student_id))
    }
    
@app.get("/employee/{name}")
def name(name:str):
    return{
        "student Name = ": name
    }
    
@app.get("/salary/{amount}")
def salary(amount:float):
    return{
        "Salary ": amount
    }
  
  
# practice  
@app.get("/book/{book_id}")
def book(book_id:int):
    return{
        "book ID " : book_id
    }
    
@app.get("/movie/{movie_name}")
def movie(movie_name:str):
    return{
        "movie name" : movie_name
    }
    
@app.get("/mobile/{brand}/{price}")
def mobile(brand:str,price:float):
    return{
        "Brand name": brand,
        "price":price
    }
    
@app.get("/result/{subject}/{marks}")
def result(subject:str,marks:int):
    return{
        "subject":subject,
        "marks":marks
    }