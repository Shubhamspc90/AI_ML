# ============================================
# Import Required Libraries
# ============================================
import os

# Load variables from .env file
from dotenv import load_dotenv

# ============================================
# Load .env File
# Is line ke baad hi os.getenv() values read karega.
# ============================================
load_dotenv()


# ============================================
# Read Database Configuration
# Future me agar password change hua to sirf
# .env change karna hoga.
# Code change nahi karna padega.
# ============================================
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")