# ============================================
# Import SQLAlchemy
# ============================================
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# ============================================
# Import Database Configuration
# ============================================
from app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME
)

# ============================================
# Create MySQL Connection URL
#
# Format:
# mysql+pymysql://username:password@host:port/database
# ============================================
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ============================================
# Create SQLAlchemy Engine
#
# Engine = Database se connection establish karta hai.
# ============================================
engine = create_engine(
    DATABASE_URL,
    echo=True      # SQL queries terminal me dikhengi
)

# ============================================
# Create Session Factory
#
# SessionLocal() se har request ke liye
# ek naya database session banega.
# ============================================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ============================================
# Base Class
#
# Saare Models isi Base ko inherit karenge.
# ============================================
Base = declarative_base()

# ============================================
# Dependency Function
#
# FastAPI request ke liye database open karega.
# Kaam hone ke baad automatically close karega.
# ============================================
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()