from external_db import fetch_articles
from internal_db import save_article
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from contextlib import asynccontextmanager
from endpoints import router
import mysql.connector
from mysql.connector import errorcode

def sync_articles():
    articles = fetch_articles()
    total_number = len(articles)
    number_of_saved = 0
    number_of_skipped = 0
    for article in articles:
        try:
            save_article(title=article["title"] ,summary=article["description"],date=article["publishedAt"].split('T')[0],author=article["author"],source=article["source"]["name"] ,url= article["url"])
            number_of_saved += 1
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_DUP_ENTRY:
                number_of_skipped += 1
            else:
                raise
    print(f"Fetched {total_number} articles")
    print(f"Save {number_of_saved} new articles")
    print(f"Skipped {number_of_skipped} duplicates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=sync_articles,trigger="interval",minutes=60)
    scheduler.start()
    yield
    scheduler.shutdown()
app = FastAPI(lifespan=lifespan)
app.include_router(router)
