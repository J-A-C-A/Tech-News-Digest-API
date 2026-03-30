from fastapi import APIRouter
from internal_db import save_tag, delete_tag
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


