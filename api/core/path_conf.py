import os
from pathlib import Path

BasePath = Path(__file__).resolve().parent.parent

ALEMBIC_VERSIONS_DIR = os.path.join(BasePath, 'alembic', 'versions')


LOG_DIR = os.path.join(BasePath, 'log')

STATIC_DIR = os.path.join(BasePath, 'static')
