from typing import List

from models.customer import CustomerModel

class CustomerRepository():
    def find_all(self) -> List[CustomerModel]:
        items = CustomerModel.scan()
        return list(items)
    
    # TODO: 他の処理を追加
