from datetime import timezone
from .database import Base
from sqlalchemy import Integer, String, Text, Column, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
    __tablename__="posts"

    id=Column(Integer, primary_key=True, nullable=False)
    title=Column(String, nullable=False)
    content=Column(Text, nullable=True, default=None)
    published=Column(Boolean, server_default="True")
    created_at=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))