import io
import os
import tempfile

from pydub import AudioSegment
import speech_recognition as sr


async def recognize(audio_data: bytes):
    audio = AudioSegment.from_file(io.BytesIO(audio_data))

    with tempfile.NamedTemporaryFile(delete=True, suffix=".wav") as temp_file:

        audio.export(temp_file.name, format="wav")
        temp_file.seek(0)
        recognizer = sr.Recognizer()

        with sr.AudioFile(temp_file.name) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="ru_RU")

            return text

