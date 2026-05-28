from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get values from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# MongoDB connection
client = MongoClient(MONGO_URI)

# Database access
db = client[DB_NAME]

# Existing Collection
users_collection = db["users"]
subjects_collection = db["subjects"]
topics_collection = db["topics"]

# Test connection
print("Database Connected Successfully")