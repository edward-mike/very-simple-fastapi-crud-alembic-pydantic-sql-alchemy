from sqlalchemy import Boolean, Column, Integer, String

from .db_connection import Model


class Article(Model):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    is_published = Column(Boolean)
    likes = Column(Integer, default=0, nullable=True)


#  Pydantic/Schema  #
#############
# title
# body
# is_published


################################################


class User(Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_valid = Column(Boolean, default=False, nullable=True)


#  Pydantic/Schema
#     username: str
#     email: str
#     password: str
#     is_valid: Optional[bool] = False
