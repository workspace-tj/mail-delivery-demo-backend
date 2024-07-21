from typing import List

from models.customer import CustomerModel
from schemas.customer import CustomerCreateRequestSchema, CustomerSchema

class CustomerRepository:
    def find_all(self) -> List[CustomerModel]:
        items = CustomerModel.scan()
        return list(items)
    
    def is_exist_by_email(self, email: str) -> bool:
        try:
            item = CustomerModel.scan(CustomerModel.email==email, limit=1)
            if not item.next():
                return False
            return True
        except StopIteration:
            return False
    
    def find_one_by_email(self, email: str)  -> CustomerModel | None:
        item = CustomerModel.scan(CustomerModel.email==email, limit=1)
        return item.next()
    
    def create_one(self, data: CustomerCreateRequestSchema) -> CustomerModel:
        item = CustomerModel(**data.model_dump())
        item.save()
        return item

    # TODO: 他の処理を追加
