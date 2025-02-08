import os
from dotenv import load_dotenv
load_dotenv()


env_file = f".env"
load_dotenv(env_file)

BACKEND_URL = os.getenv("BACKEND_URL", "redis://127.0.0.1:6379/0")
BROKER_URL=os.getenv("BROKER_URL",'redis://127.0.0.1:6379/0')