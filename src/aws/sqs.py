from typing import Any, Dict
import json

import boto3

from src.env.main import SQS_QUEUE_URL


class SQSClient:
    def __init__(self, queue_url: str = SQS_QUEUE_URL) -> None:
        self.queue_url = queue_url
        self.client = boto3.client("sqs")

    def send_message(self, message_body: Dict[str, Any]) -> Dict[str, Any]:
        response = self.client.send_message(QueueUrl=self.queue_url, MessageBody=json.dumps(message_body))
        return response
