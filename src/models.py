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
# title: str
# body: str
# is_published: Optional[bool] = False
