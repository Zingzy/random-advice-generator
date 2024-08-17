import os
from dotenv import load_dotenv

load_dotenv(override=True)

MONGO_URI = os.environ["MONGODB_URI"]
