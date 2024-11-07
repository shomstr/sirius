from pprint import pprint
from typing import BinaryIO

from yadisk import Client
from yadisk.objects import SyncResourceLinkObject

from core.conf import  get_settings

settings = get_settings()

client = Client(token=settings.YANDEX_TOKEN)

BASE_PATH = "Test"

def upload_file(file: str | bytes | BinaryIO, filename: str) -> SyncResourceLinkObject:
    with client:
        return client.upload(file, f"{BASE_PATH}/{filename}")

def download_file(file_path: str, filename: str) -> str:
    with client:
        client.download(file_path, filename)

