from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from config.api import STAGE
from utils.generate_id import generate_id

# NOTE: This is local endpoint for DynamoDB
DYNAMODB_LOCAL_ENDPOINT = "http://localhost:8000"


class CustomerModel(Model):
    class Meta:
        table_name = "Customer"
        region = "ap-northeast-1"
        if STAGE == "local":
            host = DYNAMODB_LOCAL_ENDPOINT

    id = UnicodeAttribute(hash_key=True, default=generate_id)
    email = UnicodeAttribute(range_key=True, null=False)
    username = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)
    updated_at = UTCDateTimeAttribute(default=datetime.now)
