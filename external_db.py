import os
import requests
from dotenv import load_dotenv

def fetch_articles(query):
    load_dotenv()
    key = os.getenv("API_KEY")
    articles = requests.get(url="https://newsapi.org/v2/top-headlines",params={"q":query,"apiKey":key})
    return articles.json()["articles"]

