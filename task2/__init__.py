from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth_,authorization_router,test_enpoints
from middleware import handle_exception,log_request_response
from middleware import auth_middlewar
def server_intialization():
    app=FastAPI(
        title='Authorization and Authentication Example',
        summary='Authorization and Authentication Example backend',
        version="0.1",
        docs_url='/docs',
        debug=True,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.middleware("http")(auth_middlewar)
    app.middleware("http")(log_request_response)
    app.exception_handler(Exception)(handle_exception)
    app.include_router(auth_)
    app.include_router(test_enpoints)
    app.include_router(authorization_router)
    @app.get('/heartbeat',include_in_schema=False)
    async def root():
        return "running"
    
    return app
