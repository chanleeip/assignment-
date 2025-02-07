import uvicorn
from __init__ import server_intialization
from utils.env_variables import HOST,PORT
app = server_intialization()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=int(PORT),
        reload=False,
        workers=1
    )