from dotenv import load_dotenv
import os
import mysql.connector

# Load .env vars
load_dotenv()

# Read the env vars
api_key = os.getenv("API_KEY")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

config = {
    "user": db_user,
    "password": db_password,
    "host": db_host,
    "database": db_name,
    "raise_on_warnings": True
}

# Create the connection
conn = mysql.connector.connect(**config)