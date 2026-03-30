from fastapi import APIRouter
from internal_db import save_tag, delete_tag, save_article_tag
from schemas import TagCreate

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


