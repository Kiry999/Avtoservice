import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "")
DB_NAME = os.getenv("DB_NAME", "autoservice")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")


DS_HOST_MASTER=""
DB_DSN_WRITE=f"host={DS_HOST_MASTER};"

DS_HOST_SLAVE=DS_HOST_MASTER
DB_DSN_READ=f"host={DS_HOST_SLAVE};"

