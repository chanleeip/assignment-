from fastapi import APIRouter,HTTPException,Request
test_enpoints=APIRouter()
test_routes = ["/test1", "/test2", "/test3", "/test4", "/test5", "/test6", "/test7", "/test8", "/test9", "/test10"]

for route in test_routes:
    @test_enpoints.get(route)
    async def root(request:Request):
        """
        ### Test Authentication Endpoint
        """
        try:

            return {"role":request.state.user,"user":request.state.role}   
        except Exception:
            raise HTTPException(status_code=404,detail="Error occured")
        
