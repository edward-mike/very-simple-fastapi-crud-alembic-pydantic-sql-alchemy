from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    title: str
    body: str
    is_published: Optional[bool] = False
    likes: Optional[int] = 0


# Public Exposure Schema
class ArticleResponse(Article):
    """
    Show only article title, body and likes - dont display is_published
    """

    id: int

    class Config:
        from_attributes = True


################################################################


class User(BaseModel):
    username: str
    email: str
    password: str
    is_valid: Optional[bool] = False


class UserResponse(BaseModel):
    """
    Show only user username, email - don't display password
    """

    username: str
    email: str
    is_valid: bool

    class Config:
        from_attributes = True
