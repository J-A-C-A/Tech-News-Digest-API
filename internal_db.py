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

def save_article(title, summary, date, author, source, url):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO article (title,summary,date,author,source,url) VALUES (%s,%s,%s,%s,%s,%s);"
    try:
        cursor.execute(query, (title, summary, date, author, source, url))
        db.commit()
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        db.close()