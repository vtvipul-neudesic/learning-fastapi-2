from fastapi import FastAPI, status, HTTPException, Response

from sqlalchemy.sql.functions import mode
from .database import engine
from . import models, schemas
from typing import List
# to add dependencies for fast api
from fastapi import Depends

# to create all of our models in the database
from .database import get_db

# to get Session as type
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

# creating a fast api app
app = FastAPI()


@app.get("/posts", status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post:schemas.CreatePost, db: Session = Depends(get_db)):
    newPost = models.Post(**post.dict())
    db.add(newPost)
    db.commit()
    db.refresh(newPost)
    return newPost

@app.get("/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found in the database!")
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found in the database!")
    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}", status_code=status.HTTP_200_OK)
def update_post(id: int, post: schemas.UpdatePost, db: Session = Depends(get_db)):
    update_post_query = db.query(models.Post).filter(models.Post.id == id)
    post_to_update = update_post_query.first()
    if post_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found in the database!")
    update_post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return update_post_query.first()