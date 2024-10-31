

from database.db_mysql import async_db_session, scoped_session_dependency, get_db
import secrets
import uuid
from typing import Annotated, Any
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
router = APIRouter()

class Transcription(BaseModel):
    text: str


@router.post("/transcribe")
async def transcribe(transcription: Transcription):
    print(f"Received transcription: {transcription.text}")
    return {"message": "Transcription received", "text": transcription.text}

@router.get('/')
async def root():
    return {"message": "Hello, World!"}