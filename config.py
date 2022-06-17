import os

from dotenv import load_dotenv

load_dotenv()


class MongoDBConfig:
    USERNAME = os.environ.get("MONGO_USERNAME") or "root"
    PASSWORD = os.environ.get("MONGO_PASSWORD") or "dev123"
    HOST = os.environ.get("MONGO_HOST") or "localhost"
    PORT = os.environ.get("MONGO_PORT") or "27017"
