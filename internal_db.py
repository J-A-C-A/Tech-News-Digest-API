import mysql.connector
import os
from dotenv import load_dotenv
from fastapi import HTTPException
from mysql.connector import errorcode


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
        if error.errno == errorcode.ER_DUP_ENTRY:
            pass
        else:
            raise
    finally:
        cursor.close()
        db.close()


def save_article_tag(idArticle, idTag):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO article_tag (idArticle,idTag) VALUES (%s,%s);"
    try:
        cursor.execute(query, (idArticle, idTag))
        db.commit()
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_DUP_ENTRY:
            pass
        else:
            raise
    finally:
        cursor.close()
        db.close()

def get_articles():
    db = get_connection()
    cursor = db.cursor()
    query = "SELECT * FROM article;"
    try:
        cursor.execute(query)
        articles = cursor.fetchall()
        return articles
    except mysql.connector.Error as error:
        raise
    finally:
        cursor.close()
        db.close()

def get_article_by_tag(name):
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT a.title, a.summary, a.date, a.source, a.url ,tg.name FROM article a INNER JOIN article_tag atg ON a.article_id = atg.idArticle INNER JOIN tag tg ON tg.tag_id = atg.idTag WHERE tg.name = (%s);"
    try:
        cursor.execute(query, (name,))
        articles = cursor.fetchall()
        return articles
    except mysql.connector.Error as error:
        raise
    finally:
        cursor.close()
        db.close()


def get_articles_by_date(year,month,day):
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    conditions = []
    params = []
    base_query = "SELECT a.title, a.summary, a.source, a.date, a.url FROM article a"
    if year is not None:
        conditions.append("YEAR(date) = %s")
        params.append(year)
    if month is not None:
        conditions.append("MONTH(date) = %s")
        params.append(month)
    if day is not None:
        conditions.append("DAY(date) = %s")
        params.append(day)

    if len(conditions) == 0:
        return "At least one parameter is obliged"
    else:
        base_query = base_query + " WHERE " + " AND ".join(conditions) + ";"

    try:
        cursor.execute(base_query, params)
        articles = cursor.fetchall()
        return articles
    except mysql.connector.Error as error:
        raise
    finally:
        cursor.close()
        db.close()

def get_all_articles(page: int,page_size: int):
    db = get_connection()
    cursor = db.cursor(dictionary=True)

    if page < 1 or page_size <= 0 or page_size > 100:
        raise HTTPException(status_code=400, detail="Invalid pagination parameters")

    offset = (page-1)*page_size
    query = "SELECT a.title, a.summary, a.date, a.source, a.url FROM article a ORDER BY a.date DESC, a.title ASC LIMIT %s OFFSET %s;"
    try:
        cursor.execute(query, (page_size, offset))
        articles = cursor.fetchall()
        return articles
    except mysql.connector.Error as error:
        raise
    finally:
        cursor.close()
        db.close()



def save_tag(name):
    db = get_connection()
    cursor = db.cursor()
    query = "INSERT INTO tag (name) VALUES (%s);"
    try:
        cursor.execute(query, (name,))
        db.commit()
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_DUP_ENTRY:
            pass
        else:
            raise
    finally:
        cursor.close()
        db.close()

def delete_tag(id):
    db = get_connection()
    cursor = db.cursor()
    query = "DELETE FROM tag WHERE tag_id = %s;"
    try:
        cursor.execute(query, (id,))
        db.commit()
    except mysql.connector.Error as error:
        print(error)
    finally:
        cursor.close()
        db.close()

def get_all_tags():
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM tag;"
    try:
        cursor.execute(query)
        tags = cursor.fetchall()
        return tags
    except mysql.connector.Error as error:
        raise
    finally:
        cursor.close()
        db.close()




