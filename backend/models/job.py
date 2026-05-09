from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from backend.db.database import Base 


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key = True, index = True)
    job_id = Column(String(255), nullable = False, unique = True)
    status = Column(String(50), nullable = False, default = "pending")
    session = Column(String(255), nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    theme = Column(String(255), nullable = False)
    story_id = Column(Integer, nullable = True)
    error_message = Column(Text, nullable = True)
    completed_at = Column(DateTime(timezone = True), nullable = True) 