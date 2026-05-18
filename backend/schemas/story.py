# Pydantic models for story creation and retrieval
from typing import List, Optional, Dict
from pydantic import BaseModel
from datetime import datetime

class StoryBase(BaseModel):
    text: str 
    node_id: Optional[int] = None

class StoryNodeBase(StoryBase):
    content: str
    is_end: bool = False
    is_winning: bool = False

class CompleteStoryNode(StoryNodeBase):
    id: int
    choices: List[StoryBase] = []

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme: str

class CompleteStoryResponse(BaseModel):
    id: int
    title: str 
    session: str
    created_at: datetime
    root_node: Optional[CompleteStoryNode] = None 
    all_nodes: Dict[int, CompleteStoryNode] = {} 

    class Config:
        from_attributes = True
        
        
