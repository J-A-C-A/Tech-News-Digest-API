from fastapi import APIRouter, HTTPException
from internal_db import save_tag, delete_tag, save_article_tag, get_article_by_tag, get_articles_by_date, get_all_tags, \
    get_all_articles, get_article, get_articles_by_search
from schemas import TagCreate, ArticleByTag, ArticleResponse, TagResponse, Mode
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

@router.get("/articles/date/{year}/{month}/{day}", response_model=list[ArticleResponse])
def get_articles_date(year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None):
    return get_articles_by_date(year, month, day)

@router.get("/tags", response_model=list[TagResponse])
def get_tags():
    return get_all_tags()

@router.get("/articles/{page}/{page_size}", response_model=list[ArticleResponse])
def get_articles(page: int, page_size: int):
    if page < 1 or page_size <= 0 or page_size > 100:
        raise HTTPException(status_code=400, detail="Invalid pagination parameters")
    return get_all_articles(page, page_size)

@router.get("/article/{id}", response_model=ArticleResponse)
def get_one_article(id:int):
    article = get_article(id)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

@router.get("/articles/search", response_model=list[ArticleResponse])
def get_articles_by_text(text: str, mode:Mode, page:int, page_size:int):
    if page < 1 or page_size <= 0 or page_size > 100:
        raise HTTPException(status_code=400, detail="Invalid pagination parameters")
    return get_articles_by_search(text, mode.value, page, page_size)

