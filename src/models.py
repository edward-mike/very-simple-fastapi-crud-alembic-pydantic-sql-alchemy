from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db_connection import Model


class User(Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_valid = Column(Boolean, default=False, nullable=True)
    articles = relationship("Article", back_populates="owner")


#  Pydantic/Schema
#     username: str
#     email: str
#     password: str
#     is_valid: Optional[bool] = False


class Article(Model):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    is_published = Column(Boolean)
    likes = Column(Integer, default=0, nullable=True)

    # ForeignKey to reference the owner who created the article
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    # Many-to-one relationship: A article belongs to one user
    owner = relationship("User", back_populates="articles")


#  Pydantic/Schema  #
#############
# title
# body
# is_published
