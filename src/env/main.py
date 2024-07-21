import os

from dotenv import load_dotenv

load_dotenv()

DYNAMODB_URL = os.getenv("DYNAMODB_URL")
SQS_QUEUE_URL = os.getenv("SQS_QUEUE_URL")
