import logging
from datetime import datetime

from fastapi import Request, Response
from fastapi.responses import HTMLResponse

from starlette.middleware.base import BaseHTTPMiddleware

from api.settings import Api_Dir

logger = logging.getLogger("AccessMiddleware")

class AccessMiddleware(BaseHTTPMiddleware):


    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = datetime.now()
        response = await call_next(request)
        end_time = datetime.now()
        logger.info(f'{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}')

        if response.status_code == 404:
            return HTMLResponse(content=str(Api_Dir/"templates/errors.html"), status_code=404)

        return response