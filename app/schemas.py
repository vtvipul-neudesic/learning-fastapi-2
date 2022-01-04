from pydantic import BaseModel
from datetime import datetime

# creating model for post
# such model helps fast api to auto validate the data coming in body/payload


# Through this update post model we have taken users freedom to update id and created_at attributes
# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool

# Through this model we have taken users freedom to add value to fields such as id and created_at
# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool


class PostBase(BaseModel):
    title: str
    content: str
    published: bool

    class Config:
        orm_mode = True

class PostResponse(PostBase):
    id: int
    created_at: datetime