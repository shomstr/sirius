from database.db_mysql import async_db_session, scoped_session_dependency, get_db
import secrets
import uuid
from typing import Annotated, Any
from time import time

from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel


router = APIRouter()

@router.get('/')
async def root():
    return {"message": "Welcome to Puguz team!"}