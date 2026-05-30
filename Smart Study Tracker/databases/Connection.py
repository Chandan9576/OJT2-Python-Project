from pymongo import MongoClient
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

# Load .env file
load_dotenv()

# Get values from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Debug check
print("MONGO_URI:", MONGO_URI)

# MongoDB connection
client = MongoClient(MONGO_URI)

# Database access
db = client[DB_NAME]

# Existing Collection
users_collection = db["users"]
subjects_collection = db["subjects"]
topics_collection = db["topics"]
activity_logs_collection = db["activity"]
# Test connection
print("Database Connected Successfully")


