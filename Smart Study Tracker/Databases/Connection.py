from pymongo import MongoClient

import streamlit as st

from dotenv import load_dotenv

import os


# ---------- LOAD ENV ----------

load_dotenv()


# ---------- GET MONGO URL ----------

try:

    # ----- STREAMLIT CLOUD -----

    MONGO_URL = st.secrets["MONGO_URL"]

except:

    # ----- LOCAL DEVELOPMENT -----

    MONGO_URL = os.getenv("MONGO_URI")


# ---------- DATABASE NAME ----------

DB_NAME = "smart_study_tracker"


# ---------- MONGODB CONNECTION ----------

client = MongoClient(MONGO_URL)


# ---------- DATABASE ----------

db = client[DB_NAME]


# ---------- COLLECTIONS ----------

users_collection = db["users"]

subjects_collection = db["subjects"]

topics_collection = db["topics"]

activity_logs_collection = db["activity"]


print("Database Connected Successfully")
