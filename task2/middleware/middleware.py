from fastapi import Request,HTTPException
from fastapi.responses import JSONResponse
import time
import json
from utils.logger import logger
import traceback
from starlette.concurrency import iterate_in_threadpool
async def log_request_response(request: Request, call_next):
    try:
        payload = await request.json() if request.method in ["POST", "PUT", "PATCH"] else {}
        start_time = time.time()
        logger.info(json.dumps({
            "Endpoint hit-Request": request.url.path,
            "Method": request.method,
            "Payload": payload,
        }))
        response = await call_next(request)
        process_time = time.time() - start_time
        response_body = [chunk async for chunk in response.body_iterator]
        response.body_iterator = iterate_in_threadpool(iter(response_body))
        logger.info(json.dumps({
            "Endpoint hit-Response": request.url.path,
            "Method": request.method,
            "Payload": payload,
            "response_status_code": response.status_code,
            "processed_time": f"{process_time:.2f} seconds"
        }))
        return response
    except Exception as e:
        return await handle_exception(request, e)

async def handle_exception(request: Request, exc: Exception):
    tb_str = traceback.format_exc().splitlines() 
    logger.error(json.dumps({
        "message": "An error occurred",
        "traceback": tb_str
    }))
    status_code = 500  
    content = {"error": "An internal error occurred"}

    # Handle HTTPException specifically
    # if isinstance(exc, HTTPException):
    #     status_code = exc.status_code
    #     content = {"detail": exc.detail}

    return JSONResponse(
        status_code=status_code,
        content=content
    )