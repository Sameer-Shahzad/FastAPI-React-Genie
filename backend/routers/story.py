from typing import Optional
from urllib import response
import uuid

from requests import Session
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from backend.db.database import SessionLocal, get_db
from backend.models.story import Story, Node
from backend.models.job import Job, JobStatus
from backend.schemas.story import CreateStoryRequest, CompleteStoryResponse, CompleteStoryNode
from datetime import datetime
from backend.schemas.job import CreateJobRequest



router = APIRouter(
    prefix = "/stories",
    tags = ["stories"]
)

def get_session_id(session_id: Optional[str] = Cookie(None)) -> str:
    if session_id is None:
        session_id = str(uuid.uuid4())
    return session_id


@router.post(path="/create", response_model=CompleteStoryResponse)
def create_story(
    request: CreateStoryRequest, 
    session_id: str = Depends(get_session_id), 
    db: Session = Depends(get_db), 
    background_tasks: BackgroundTasks = None
):
    response.set_cookie(key="session_id", value=session_id, httponly=True)
    job_id = str(uuid.uuid4())
    job = Job(
        job_id = job_id,
        session = session_id,
        theme = request.theme,
        status = JobStatus.PENDING.value
    )
    db.add(job)
    db.commit()
    db.refresh(job)     
    
    return job


def genrate_story(job_id: str, db: Session):
    job = db.query(Job).filter(Job.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    try:
        generated_story_id = 1 
        job.story_id = generated_story_id
        job.status = JobStatus.COMPLETED.value
        job.completed_at = datetime.utcnow()
        db.commit()
    except Exception as e:
        job.status = JobStatus.FAILED.value
        job.error_message = str(e)
        db.commit()