from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
    return {
        "message":"Hello API"
    }
    
@app.get("/about")
def about():
    return{
        "company":"OpenAI",
        "course":"FastAPI",
        "Language":"Python"
    }
    
@app.get("/student")
def student():
    return {
        "Name" : "Shubham Chauahn",
        "Roll" : 101 ,
        "age"  : 24,
        "course":{
            1:"mca",
            2:"bca",
            3:"mba"
        }
    }

@app.get("/teacher")
def teacher():
    return{
        "name" : "Varun",
        "UID"  : 12416297,
        "salary" : 50000.5,
        "active" : True
        
    }
    
@app.get("/employee")
def employee():
    return{
        "id":"500",
        "name":"Dhar",
        "Department":"LAW",
        "salary":"120000"
    }
    
    
@app.get("/mobile")
def mobile():
    return{
        "brand": "Samsung",
        "model": "S25",
        "specification": {
            "ram": "12GB",
            "storage": "256GB",
            "processor": "Snapdragon"
    }
    }
    
@app.get("/car")
def car():
    return{
        "brand" : "BMW",
        "model" : "X5",
        "engine" : {
            "type":{
                "type1" : "Petrol",
                "type2" : "Disel",
                "type3" : "Electical"
            },
            "power":"300 HP"      
        }
    }
    
# (List Response)
@app.get("/fruits")
def fruits():
    return [
        "apple",
        "banana",
        "orange"
    ]
    
    
@app.get("/number")
def numbers():
    return [
        10,20,30,40,50
    ]

# (List of Objects)

@app.get("/students")
def students():
    return[
        {
            "id": 1,
            "name": "Shubham"
        },
        {
            "id":2,
            "name":"dhar"
        },
        {
            "id":3,
            "name":"VCP"
        },
        {
            "id":4,
            "name":"DSP"
        }
    ] 
    
    
@app.get("/books")
def books():
    return[
        {
            "title":"python",
            "price":500
        },
        {
            "title":"JAVA",
            "price":600
        }
    ]
    
@app.get("/movies")
def movies():
    return{
        "id":"01",
        "movie":"Madaari",
        "Actor": "Irfan Khan",
        "song":"Masoom Sa",
        "Date":2012,
        "rating":5.0
    }
    
# Return a list of 5 employee objects.
@app.get("/Employees")
def Employee():
    return[
        {
            "id":1,
            "name":"Shubham",
            "department":"IT",
            "salary":1000000
        },
        {
            "id":2,
            "name":"Dhar",
            "department":"HR",
            "salary":300000
        },
        {
            "id":3,
            "name":"Varun",
            "department":"IT",
            "salary":5000000
        },
        {
            "id":4,
            "name":"DSP",
            "department":"Electical",
            "salary":200000
        },
        {
            "id":5,
            "name":"VCP",
            "department":"Sales",
            "salary":150000
        },
        {
            "id":6,
            "name":"Dipti",
            "department":"Marketing",
            "salary":50000
        },
    ]
