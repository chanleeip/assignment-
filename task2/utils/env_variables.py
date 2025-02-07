import os
from dotenv import load_dotenv
load_dotenv()


env_file = f".env"
load_dotenv(env_file)

HOST = os.getenv("HOST", "127.0.0.1")
PORT=os.getenv("PORT",'3000')
SECRET_KEY= os.getenv("SECRET_KEY", "63xxx79")
JWT_ENCODE_ALGORITHM= os.getenv("JWT_ENCODE_ALGORITHM", "HS256")