from aws_lambda_powertools.event_handler.exceptions import InternalServerError

from schemas.email_request import EmailRequestSchema
from schemas.main import MessageSchema
from services.email_request import EmailRequestService


class EmailRequestController:
    def __init__(self) -> None:
        self.email_request_service = EmailRequestService()

    def queue_email_requests_to_customer_all(self, email_request: EmailRequestSchema) -> MessageSchema:
        if not self.email_request_service.queue_email_requests_to_customer_all(email_request):
            raise InternalServerError(message="")
        return MessageSchema(message="request send to queue successfully")
