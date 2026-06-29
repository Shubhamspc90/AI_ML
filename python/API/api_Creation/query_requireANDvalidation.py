from fastapi import FastAPI,Query
app=FastAPI()

# Example 1: Required Query Parameter
#  Query(...) => name dena hi padega.
@app.get("/name")
def name(name:str=Query(...)): 
    return{
        "Name":name
    }
    
# Example 2: Required + Validation
@app.get("/employee")
def employee(name: str = Query(..., min_length=3, max_length=20 )):
    return {
        "Employee": name
    }
    
# Example 3: Multiple Required Parameters
@app.get("/student")
def student(
    name: str = Query(...),
    age: int = Query(...)
):
    return {
        "Name": name,
        "Age": age
    }
    
# Real World Example
"""Suppose tum Flipkart ki API bana rahe ho.
Product search ke liye category compulsory hai."""

@app.get("/products")
def get_products(
    category: str = Query(...),
    brand: str | None = Query(None),
    price: int | None = Query(None)
):
    return {
        "Category": category,
        "Brand": brand,
        "Price": price
    }
    
    
"""What is the difference between Query(...), Query(None), and Query("Guest")?"""

'''
Query(...) → Required parameter (must be provided).
Query(None) → Optional parameter with None as the default.
Query("Guest") → Optional parameter with a custom default value ("Guest").
'''

#practice
# Create an API:
@app.get("/login")
def login(userName:str=Query(...),
          password:str=Query(...),
          rememberMe:bool=Query(False)):
    return{
        "User Name":userName,
        "Remember Me":rememberMe
        }
 

#practice   
@app.get("/settings")
def settings(
    dark_mode: bool = Query(False),
    notifications: bool = Query(True)
):
    return {
        "Dark Mode": dark_mode,
        "Notifications": notifications
    }
# Isko ye URLs se test karo:   
#1.  /settings
#2.  /settings?dark_mode=true
#3.  /settings?notifications=false
#4.  /settings?dark_mode=true&notifications=false