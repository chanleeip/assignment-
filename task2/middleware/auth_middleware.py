from fastapi import Request,HTTPException,Response
from fastapi.encoders import jsonable_encoder
from typing import Optional,Dict,Any
from fastapi.responses import JSONResponse
import datetime
import traceback
from utils.logger import logger
import json
import jwt
from jwt.exceptions import InvalidTokenError
from utils.env_variables import SECRET_KEY,JWT_ENCODE_ALGORITHM

def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ENCODE_ALGORITHM])
        return payload.get('username','username'),payload.get('role','admin')
    except InvalidTokenError:
        raise Exception("Bearer Token is Invalid" )
    
def create_jwt_token(payload: Dict[str, Any], expiration_minutes: int = 60) -> str:
    try:
        if not payload["username"] or not payload["password"]:
            return {"status":"failure","msg":"username or password missing"}
        expire_time = datetime.datetime.now() + datetime.timedelta(minutes=expiration_minutes)
        payload["exp"] = expire_time
        encoded_token = jwt.encode(payload, SECRET_KEY, algorithm=JWT_ENCODE_ALGORITHM)
        return {
            "token":encoded_token,
            "expiry_time":60*60
        }
    except Exception as e:
        raise  Exception(
        f"Could not create the token {e}",
        )
    
async def auth_middlewar(request: Request, call_next):
    try:
        if request.url.path in ["/docs", "/openapi.json","/login"]:
            return await call_next(request)
        auth_header = request.headers.get("Authorization")
        if auth_header:
            if not auth_header.startswith("Bearer "):
                 raise  Exception(
                        f"Invalid or expired token",
                    )
            token = auth_header.split(" ")[1]
            username,role = decode_jwt_token(token)
            request.state.user = username
            request.state.role = role           # request.state.role = role
            return await call_next(request)
        else:
            raise  Exception(
                        f"Authorization Header missing",
                    )
    except Exception as e:
        with open("hehess.txt",'w') as f:
                f.write("fcsssk")   
        return JSONResponse(
                    status_code=404,
                    content={
                        "error":str(e)
                    },
                )