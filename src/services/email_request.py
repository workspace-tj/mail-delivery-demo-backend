import json
from typing import List

from aws.sqs import SQSClient
from schemas.customer import CustomerSchema
from schemas.email_request import EmailRequestSchema
from services.customer import CustomerService


class EmailRequestService:
    def __init__(self) -> None:
        self.customer_service = CustomerService
        self.sqs_client = SQSClient

    def queue_email_requests(self, email_request: EmailRequestSchema, customers: List[CustomerSchema]) -> bool:
        try:
            for customer in customers:
                message_body = {
                    "emailType": email_request.email_type,
                    "subject": email_request.subject,
                    "text": email_request.text,
                    "html_text": email_request.html_text,
                    "customer": customer,
                }
                self.sqs_client.send_message(message_body=json.dumps(message_body))
            return True
        except Exception as e:
            print(f"Failed to queue email requests: {str(e)}")
            return False

    def queue_email_requests_to_customer_all(self, email_request: EmailRequestSchema) -> bool:
        customers = self.customer_service.find_all()
        return self.queue_email_requests(email_request, customers)
