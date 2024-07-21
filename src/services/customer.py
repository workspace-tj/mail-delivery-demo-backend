from typing import List

from aws_lambda_powertools.event_handler.exceptions import BadRequestError

from models.customer import CustomerModel
from repositories.customer import CustomerRepository
from schemas.customer import CustomerSchema, CustomerCreateRequestSchema


class CustomerService:
    def __init__(self) -> None:
        # CustomerRepositoryをインスタンス化
        self.customer_repository = CustomerRepository()

    def find_all(self) -> List[CustomerSchema]:
        items = self.customer_repository.find_all()
        return [item.serializer() for item in items]
    
    def is_exist_by_email(self, email: str) -> bool:
        return self.customer_repository.is_exist_by_email(email) # type: ignore

    def find_one_by_email(self, email: str) -> CustomerSchema | None:
        item = self.customer_repository.find_one_by_email(email)
        if not item: return None
        return item.serializer()

    def create_one(self, data: CustomerCreateRequestSchema) -> CustomerSchema:
        if self.customer_repository.is_exist_by_email(data.email):
            raise BadRequestError("email already used")
        item = self.customer_repository.create_one(data)
        return item.serializer()
