from fastapi import APIRouter,Request,HTTPException
from utils.logger import logger
authorization_router= APIRouter()
import traceback

data={
    "admin": [{"id": 1, "name": "Project A"}, {"id": 2, "name": "Project B"}],
    "user": [{"id": 3, "name": "Project C"}]
}
@authorization_router.get(
        path="/authorization-demo",
        status_code=200,
        tags=["Auth-POST-request"],
        summary="This is used to mimic authorization using some dummy values",
        )
async def root(request:Request):
    """
    Authorization mimicing
    """
    try:
        return {"role":request.state.role,"username":request.state.user,"data":data[request.state.role]}   
    except Exception as e:
        raise HTTPException(status_code=404,detail=traceback.format_exc().splitlines())