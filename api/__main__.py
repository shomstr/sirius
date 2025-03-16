import asyncio
import logging


from api.config import app
from api.settings import settings
from api.utils.connect_to_services import test_redis_pool, test_database_pool
from api.utils.log import init_logger
from api.handlers import setup_routers
from api.middlewares import setup_middlewares

init_logger()
logger = logging.getLogger(__name__)

import logging


def _main() -> None:
    logger.info("Starting api...")

    # if settings.redis.use:
    #     try:
    #         test_redis_pool()
    #     except ConnectionError as e:
    #         logger.error(
    #             "Failed connection to Redis",
    #             e,
    #         )
    #         exit(1)
    # try:
    #     test_database_pool()
    # except ConnectionRefusedError as e:
    #     logger.error(
    #         "Failed connection to %s: %s",
    #         settings.db.used,
    #         e,
    #     )
    #     exit(1)

    setup_middlewares(app)
    setup_routers(app)


    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

def main() -> None:
    _main()


if __name__ == "__main__":
    main()
