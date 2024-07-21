from typing import List

from models.customer import CustomerModel
from repositories.customer import CustomerRepository
from schemas.customer import CustomerSchema


class CustomerService:
    def __init__(self) -> None:
        # CustomerRepositoryをインスタンス化
        self.customer_repository = CustomerRepository()

    def find_all(self) -> List[CustomerSchema]:
        items = self.customer_repository.find_all()
        return [CustomerModel(**item) for item in items]
