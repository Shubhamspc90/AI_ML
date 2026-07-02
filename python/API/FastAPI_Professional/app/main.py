# =====================================================
# Import FastAPI
# =====================================================

from fastapi import FastAPI

# Database
from app.database import Base, engine

# Models
from app import models

# Import Student Router
from app.routers import students


# =====================================================
# Create Tables
# =====================================================

Base.metadata.create_all(bind=engine)


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI(

    title="Student Management API",

    description="Professional FastAPI Project",

    version="1.0.0"

)

# =====================================================
# Register Router
#
# Ab students.py ki saari APIs
# application ka part ban jayengi.
# =====================================================

app.include_router(students.router)


# =====================================================
# Home API
# =====================================================

@app.get("/")
def home():

    return {

        "message": "Welcome to Professional FastAPI"

    }