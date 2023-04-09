import os
from dotenv import load_dotenv

# Automatic search .env file
load_dotenv(verbose=True)


# redis config
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
REDIS_DB_INDEX = os.getenv('REDIS_DB')
