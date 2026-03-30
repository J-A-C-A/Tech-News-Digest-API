from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional
class TagCreate(BaseModel):
    name: str

class ArticleByTag(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    title: str
    summary: Optional[str] = None
    date: date
    source: str
    tag_name: str = Field(alias="name")