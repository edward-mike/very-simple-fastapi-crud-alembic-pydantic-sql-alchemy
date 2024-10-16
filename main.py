from typing import Dict, List

from fastapi import Depends, FastAPI, HTTPException, Response, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src import models, schema
from src.db_connection import Model, engine, get_db_session

app = FastAPI()


Model.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 1. General Welcome Route
@app.get("/")
def welcome_api() -> Dict[str, str]:
    """Handler for / route"""
    return {"message": "How to use API"}


# 2. Create Article
@app.post("/create-article", status_code=status.HTTP_201_CREATED, tags=["article"])
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
@app.get(
    "/articles/",
    status_code=status.HTTP_200_OK,
    response_model=List[schema.ArticleResponse],
    tags=["article"],
)
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
@app.get(
    "/article/{id}",
    status_code=status.HTTP_200_OK,
    response_model=schema.ArticleResponse,
    tags=["article"],
)
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
@app.put("/article/edit/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["article"])
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
@app.delete(
    "/article/delete/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["article"]
)
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


########################################################################################


# Create User
@app.post("/create-user", status_code=status.HTTP_201_CREATED, tags=["user"])
def create_user(
    user: schema.User, session: Session = Depends(get_db_session)
) -> schema.User:
    hashed_password = pwd_context.hash(user.password)

    user = models.User(
        username=user.username, email=user.email, password=hashed_password
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


# Get All Users
@app.get(
    "/users/",
    status_code=status.HTTP_200_OK,
    response_model=List[schema.UserResponse],
    tags=["user"],
)
def users(
    response: Response, session: Session = Depends(get_db_session)
) -> List[schema.User]:
    """Handler for retrieving all users"""
    users = session.query(models.User).all()
    if not users:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": "Users not found"}
    return users
