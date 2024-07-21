from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from utils.generate_id import generate_id


class CustomerModel(Model):
    class Meta:
        table_name = "Customer"

    id = UnicodeAttribute(hash_key=True, default=generate_id)
    email = UnicodeAttribute(range_key=True, null=False)
    username = UnicodeAttribute(range_key=True)
    created_at = UTCDateTimeAttribute(default=datetime.now)
    updated_at = UTCDateTimeAttribute(default=datetime.now)
