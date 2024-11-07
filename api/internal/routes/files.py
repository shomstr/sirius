import pydub
from fastapi import UploadFile, File, APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from database.db_mysql import get_db
from models import UserFile
from services import yandex_disk, transcribe, summarize
import speech_recognition
router = APIRouter()

@router.post("/upload_file")
async def upload_file(user_id: int, file: UploadFile = File(), db: AsyncSession = Depends(get_db)):
    file_suffix = file.filename.split(".")[-1]
    new_file_db = await UserFile.create_user_file(db, user_id, file.filename)
    file_name = f"{new_file_db.id}.{file_suffix}"

    yandex_disk.upload_file(file.file, file_name)

    return {"success"}


@router.get("/get_uploads_files/{user_id}")
async def get_uploads_files(user_id: int, db: AsyncSession = Depends(get_db)):
    user_files = await UserFile.get_user_uploads_files(db, user_id)
    return {
        file.id: {
            "filename": file.file_name,
            "upload_at": file.upload_at
        } for file in user_files}


@router.post("/transcribe")
async def transcribe_file(file: UploadFile = File()):
    audio_data = await file.read()
    try:
        text = await transcribe.recognize(audio_data)
        summ = summarize.translate_and_summarize(text)
        return JSONResponse(content={"transcription": text, "summ": summ})
        
    except pydub.exceptions.CouldntDecodeError:
        return JSONResponse(content={"error": f"Ошибка при обработке аудио"}, status_code=400)
    except speech_recognition.UnknownValueError:
        return JSONResponse(content={"error": "Не удалось распознать аудио"}, status_code=400)
    except speech_recognition.RequestError as e:
        return JSONResponse(content={"error": f"Ошибка сервиса: {e}"}, status_code=500)
    

