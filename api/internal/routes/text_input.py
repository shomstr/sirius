import pydub
from fastapi import UploadFile, File, APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from pydantic import BaseModel
from database.db_mysql import get_db
from models import UserFile
from services import yandex_disk, transcribe, summarize
import speech_recognition
router = APIRouter()

class TextInput(BaseModel):
    text: str


@router.post("/submit-text")
async def submit_text(input_data: TextInput, db: AsyncSession = Depends(get_db)):
    try:
        summ = summarize.translate_and_summarize(input_data.text)
        return {"message": summ}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Произошла ошибка: {str(e)}"
        )