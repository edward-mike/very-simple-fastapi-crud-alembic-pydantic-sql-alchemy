from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from src import models, schema
from src.db_connection import get_db_session

app = FastAPI()


# 1. General Welcome Route
@app.get("/")
def welcome_api() -> Dict[str, str]:
    """Handler for / route"""
    return {"message": "How to use API"}


# 2. Create Article
@app.post("/create-article", status_code=status.HTTP_201_CREATED)
def create_article(
    article: schema.Article, session: Session = Depends(get_db_session)
) -> schema.Article:
    """Handler for creating a new article"""
    article = models.Article(**vars(article))
    session.add(article)
    session.commit()
    session.refresh(article)
    return article


# 3. Get All Articles
@app.get("/articles/", status_code=status.HTTP_200_OK)
def articles(
    response: Response, session: Session = Depends(get_db_session)
) -> List[schema.Article]:
    """Handler for retrieving all articles"""
    articles = session.query(models.Article).all()
    if not articles:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Articles not found"}
    return articles


# 4. Get a Single Article by ID
@app.get("/article/{id}", status_code=status.HTTP_200_OK)
def article(
    id: int, response: Response, session: Session = Depends(get_db_session)
) -> schema.Article:
    """Handler for retrieving an article by ID"""
    article = session.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id `{id}` not found",
        )
    return article


# 5. Update an Article by ID
@app.put("/article/edit/{id}", status_code=status.HTTP_202_ACCEPTED)
def article_update(
    id: int, article: schema.Article, session: Session = Depends(get_db_session)
) -> str:
    """Handler for updating an article by ID"""
    article_db = session.query(models.Article).filter(models.Article.id == id).first()
    if not article_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id `{id}` not found",
        )
    for key, value in vars(article).items():
        setattr(article_db, key, value)

    session.commit()
    session.refresh(article_db)
    return "updated"


# 6. Delete an Article by ID
@app.delete("/article/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def article_delete(
    id: int, response: Response, session: Session = Depends(get_db_session)
) -> None:
    """Handler for deleting an article by ID"""
    article = session.query(models.Article).filter(models.Article.id == id).first()
    if not article:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Article with id `{id}` not found",
        )
    session.delete(article)
    session.commit()
