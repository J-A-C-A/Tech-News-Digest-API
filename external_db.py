import os
import requests
from dotenv import load_dotenv

def fetch_articles():
    load_dotenv()
    key = os.getenv("API_KEY")
    response = requests.get(url="https://newsapi.org/v2/top-headlines",params={"category":"technology","apiKey":key,"language":"en"})
    data = response.json()
    if data["status"] != "ok":
        print("API doesn't work", data.get("message"))
    if data["totalResults"] > 0:
        print("There are some articles")
    return data.get("articles",[])

