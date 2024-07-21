from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from router import email_request

from models.customer import CustomerModel

if not CustomerModel.exists():
    CustomerModel.create_table(wait=True, billing_mode="PAY_PER_REQUEST")

app = APIGatewayRestResolver(enable_validation=True)
app.use(middlewares=[])
app.include_router(router=email_request.router, prefix="/email-request")


def lambda_handler(event: dict, context: LambdaContext) -> dict[str, str | int]:
    return app.resolve(event, context)
