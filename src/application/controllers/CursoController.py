from database import get_db
from database import engine, Base
from sqlalchemy.orm import Session
from domain.models.social_worker import SocialWorkerResponse, SocialWorkerRequest
from domain.models.social_worker import SocialWorker, SocialWorkerDB
from security import get_password_hash
from fastapi import APIRouter, Depends, status, HTTPException, Response
from interfaces.controllersi import socialWorkerService

Base.metadata.create_all(bind=engine)


router = APIRouter(
    prefix="/socialWorker",
    tags=["socialWorker"]
)