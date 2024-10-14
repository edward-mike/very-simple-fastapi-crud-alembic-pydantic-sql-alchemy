from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    body: str
    is_published: Optional[bool] = False
    likes: Optional[int] = 0
