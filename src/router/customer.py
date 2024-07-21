from typing import List

from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router

from controllers.customer import CustomerController
from schemas import errors
from schemas.customer import CustomerCreateRequestSchema, CustomerSchema

app = APIGatewayRestResolver(debug=True)
router = Router()

controller = CustomerController()

@router.get("/", tags=["Customer"], summary="顧客の全取得", description="""
## 概要

顧客データを全取得

## 変更履歴

""",
    response_description="顧客を全取得",
    operation_id="getCustomersAll",
    responses={
        200: {"description": "顧客を全取得"},
        400: errors.BAD_REQUEST_ERROR,
        401: errors.UNAUTHORIZED_ERROR,
        404: errors.NOT_FOUND_ERROR,
        500: errors.INTERNAL_SERVER_ERROR,
    },
)
def find_all() -> List[CustomerSchema]:
    return controller.find_all()  # type: ignore


@router.post(
    "/",
    tags=["Customer"],
    summary="顧客の作成",
    description="""
## 概要

顧客データを作成

## 変更履歴

""",
    response_description="顧客を作成",
    operation_id="createCutomerData",
    responses={
        201: {"description": "顧客を作成"},
        400: errors.BAD_REQUEST_ERROR,
        401: errors.UNAUTHORIZED_ERROR,
        404: errors.NOT_FOUND_ERROR,
        500: errors.INTERNAL_SERVER_ERROR,
    },
)
def create_one(data: CustomerCreateRequestSchema) -> CustomerSchema:
    return controller.create_one(data)  # type: ignore
