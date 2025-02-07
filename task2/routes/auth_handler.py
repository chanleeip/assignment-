from fastapi import APIRouter
from schemas import AuthRequesteModel,AuthResponseModel
from middleware import create_jwt_token
auth_= APIRouter()

@auth_.post(
        path="/login",
        status_code=200,
        tags=["Auth-POST-request"],
        summary="This is used to Login and create a Bearer token",
        description="""
                    using username and password, it returns a bearer token to be used with api's for authentication
                """,
        response_description="Returns a Bearer Token",
        name="auth-api",
        responses={
            200: {
            "token": "xxxxxxxxxxx",
            "expiry_time":3600
        },
        400: {
            "error":"Invalid Format. Failed to create Bearer Token"
        },
        500: {
            "error":"Internal Server Error. Failed to create Bearer Token"
    }
        }
        )
async def root(
    request:AuthRequesteModel,
    ):
    """
    ### BEarer token Creation Endpoint
    This endpoint allows users to create a trigger.
    """
    try:
        token=create_jwt_token(request.model_dump(),expiration_minutes=60)
        return token
    except Exception as e:
        return AuthResponseModel(
            error=f"Failed to create BEarer token {str(e)}"
        )