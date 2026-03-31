from fastapi import APIRouter
from internal_db import save_tag, delete_tag, save_article_tag, get_article_by_tag, get_articles_by_date, get_all_tags
from schemas import TagCreate, ArticleByTag, ArticleResponse, TagResponse
from typing import Optional
router = APIRouter()

@router.get("/")
def index():
    return {"message":"Hello World"}

@router.post("/add_tag")
def add_tag(Tag: TagCreate):
    save_tag(Tag.name)
    return {"message":"tag added successfully"}

@router.delete("/remove_tag/{id}")
def remove_tag(id: int):
    delete_tag(id)
    return {"message":"tag removed successfully"}

@router.post("/connect_tag_article/{article_id}/{tag_id}")
def connect_tag_article(article_id: int, tag_id: int):
    save_article_tag(article_id, tag_id)
    return {"message":"tag connected to article successfully"}

@router.get("/articles/tag/{tag_name}", response_model=list[ArticleByTag], response_model_by_alias=False)
def get_article_tag(tag_name: str):
    return get_article_by_tag(tag_name)

@router.get("/articles/date", response_model=list[ArticleResponse])
def get_articles_date(year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None):
    return get_articles_by_date(year, month, day)

@router.get("/tags", response_model=list[TagResponse])
def get_tags():
    return get_all_tags()


