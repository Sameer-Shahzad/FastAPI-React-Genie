from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Json
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.db.database import Base 

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(255), nullable = False)
    session = Column(String(255), nullable = False, unique = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    nodes = relationship(argument = "Node", back_populates = "story", cascade = "all, delete-orphan")
    

class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key = True, index = True)
    story_id = Column(Integer, ForeignKey("stories.id"), nullable = False)
    content = Column(Text, nullable = False)
    is_root = Column(Boolean, default = False)
    story = relationship(argument = "Story", back_populates = "nodes")
    is_end = Column(Boolean, default = False)
    is_winning = Column(Boolean, default = False)
    choices = Column(Json, nullable = True)

    