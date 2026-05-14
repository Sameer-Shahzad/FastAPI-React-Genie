from typing import Optional
import uuid
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from backend.db.database import SessionLocal, get_db
from backend.models.story import Story, Node
from backend.models.job import Job, JobStatus
from backend.schemas.story import CreateStoryRequest, CompleteStoryResponse, CompleteStoryNode
from datetime import datetime
from backend.schemas.job import CreateJobRequest