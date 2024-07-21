from typing import Any

import boto3

from src.env.main import SQS_QUEUE_URL


class SQSClient:
    def __init__(self, queue_url: str = SQS_QUEUE_URL) -> None:
        self.queue_url = queue_url
        self.client = boto3.client("sqs")

    def send_message(self, message_body: dict[str, Any]):
        self.client.send_message(QueueUrl=self.queue_url, MessageBody=message_body)
