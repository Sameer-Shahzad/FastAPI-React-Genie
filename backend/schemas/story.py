from typing import List, Optional, Dict, Any
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
    options: List[StoryBase] = []
    
    class Config:
        from_attributes = True
        

class CreateStoryRequest(BaseModel):
    theme: str


class CompleteStoryResponse(BaseModel):
    id: int
    created_at: datetime
    root_node: CompleteStoryNode
    all_nodes: Dict[int, CompleteStoryNode] = []
    
    class Config:
        from_attributes = True