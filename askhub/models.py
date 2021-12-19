from datetime import datetime
import enum

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from askhub.database import Base


class PostType(enum.Enum):
    QUESTION = 1
    ANSWER = 2


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    body = Column(String(1000))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    post_type_id = Column(Enum(PostType))
    parent_id = Column(Integer, ForeignKey('posts.id'))

    def __init__(self, title="", body="", type_id=PostType.QUESTION, parent_id=None):
        self.title = title
        self.body = body
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.post_type_id = type_id
        self.parent_id = parent_id

    def __repr__(self):
        return f'<Post {self.id!r}>'