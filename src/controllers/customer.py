
from http import HTTPStatus
from typing import List

from aws_lambda_powertools.event_handler.exceptions import NotFoundError

from schemas.customer import CustomerCreateRequestSchema, CustomerSchema
from services.customer import CustomerService


class CustomerController:

    def __init__(self) -> None:
        self.service = CustomerService()

    def find_all(self) -> List[CustomerSchema]:
        return self.service.find_all()  # type: ignore

    def find_one_by_email(self, email: str) -> CustomerSchema:
        if not self.service.is_exist_by_email(email):
            raise NotFoundError("Customer not found")
        return self.service.find_one_by_email(email)

    def create_one(self, data: CustomerCreateRequestSchema) -> CustomerSchema:
        return self.service.create_one(data), HTTPStatus.CREATED
