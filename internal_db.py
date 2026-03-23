import mysql.connector
import os
from dotenv import load_dotenv

def get_connection():
    load_dotenv()
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    name = os.getenv("DB_NAME")
    mydb = mysql.connector.connect(host=host, user=user, password=password, database=name)
    return mydb

