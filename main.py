from external_db import fetch_articles
from internal_db import save_article
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from contextlib import asynccontextmanager
from endpoints import router

def sync_articles():
    query = "technology"
    articles = fetch_articles(query)

    for article in articles:
        save_article(title=article["title"] ,summary=article["description"],date=article["publishedAt"].split('T')[0],author=article["author"],source=article["source"]["name"] ,url= article["url"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=sync_articles,trigger="interval",minutes=60)
    scheduler.start()
    yield
    scheduler.shutdown()
app = FastAPI(lifespan=lifespan)
app.include_router(router)
