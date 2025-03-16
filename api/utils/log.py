from __future__ import annotations

import logging
from datetime import datetime
from logging import LogRecord, StreamHandler
from logging.handlers import RotatingFileHandler

from api.config import DEFAULT_TZ
from api.settings import settings, LogDir

TIME_FORMAT = "%Y-%m-%d"
# Formatters
MAIN_FORMATTER = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s]: %(name)s: %(message)s",
    datefmt="%H:%M:%S",
    style="%",
)


class DailyRotatingFileHandler(RotatingFileHandler):
    def __init__(
        self,
        mode: str = "a",
        maxBytes: int = 0,  # noqa: N803
        backupCount: int = 0,  # noqa: N803
        encoding: str | None = None,
        delay: bool = False,
    ) -> None:
        self.baseFilename = self.get_filename()
        self.today = self._today()
        RotatingFileHandler.__init__(self, self.baseFilename, mode, maxBytes, backupCount, encoding, delay)

    def _today(self) -> datetime:
        self.today = datetime.now()
        return self.today

    @staticmethod
    def get_filename() -> str:
        """
        @summary: Return logFile name string formatted to "today.log.alias"
        """
        today = datetime.now(DEFAULT_TZ)
        file_name = today.strftime(TIME_FORMAT) + ".log"
        return str(LogDir / file_name)

    def shouldRollover(self, record: LogRecord) -> int:  # noqa: N802
        """
        @summary:
        Rollover happen
        1. When the logFile size is get over maxBytes.
        2. When date is changed.

        @see: BaseRotatingHandler.emit
        """

        if self.stream is None:
            self.stream = self._open()

        if int(self.maxBytes) > 0:
            msg = f"{self.format(record)}\n"
            self.stream.seek(0, 2)
            if self.stream.tell() + len(msg) >= int(self.maxBytes):
                return 1

        if self.today != self._today:
            self.baseFilename = self.get_filename()
            return 1

        self.baseFilename = self.get_filename()
        return 0



def _get_daily_handler() -> DailyRotatingFileHandler:
    daily_handler = DailyRotatingFileHandler()
    daily_handler.setFormatter(MAIN_FORMATTER)
    daily_handler.setLevel(logging.DEBUG)

    return daily_handler



def _get_console_handler() -> StreamHandler:
    console_level = logging.DEBUG

    console_handler = StreamHandler()
    console_handler.setFormatter(MAIN_FORMATTER)
    console_handler.setLevel(console_level)
    return console_handler


def init_logger() -> None:
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().handlers = []
    logging.getLogger().addHandler(_get_daily_handler())
    logging.getLogger().addHandler(_get_console_handler())

    logging.getLogger("asyncio").setLevel(logging.ERROR)
    logging.getLogger("apscheduler").setLevel(logging.ERROR)
    logging.getLogger("tzlocal").setLevel(logging.ERROR)