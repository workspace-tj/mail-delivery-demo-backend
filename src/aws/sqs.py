from typing import Any, Dict
import json

import boto3

from src.env.main import SQS_QUEUE_URL
from config.api import STAGE


class SQSClient:
    def __init__(self, queue_url: str = SQS_QUEUE_URL) -> None:
        self.queue_url = queue_url
        if STAGE == "local":
            session = boto3.session.Session()
            self.client=session.client(
                service_name='sqs',
                aws_access_key_id='aaa',
                aws_secret_access_key='bbb',
                endpoint_url=SQS_QUEUE_URL,
                )
            return
        self.client = boto3.client("sqs")


    def send_message(self, message_body: Dict[str, Any]) -> Dict[str, Any]:
        # FIXME: queurl
        response = self.client.send_message(QueueUrl=self.queue_url + "/test-que", MessageBody=json.dumps(message_body))
        return response
