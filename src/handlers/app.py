from typing import List

from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.event_handler.openapi.models import  Server

from models.customer import CustomerModel
from router import email_request, customer
from config.api import STAGE

if not CustomerModel.exists():
    CustomerModel.create_table(wait=True, billing_mode="PAY_PER_REQUEST")

app = APIGatewayRestResolver(enable_validation=True)
app.use(middlewares=[])
app.include_router(router=customer.router, prefix="/customer")
app.include_router(router=email_request.router, prefix="/email-request")

local_server = Server(
    url="http://localhost:3333", description="Local Development Server", variables=None
)
dev_server = Server(
    url="APP_API_BASE_URL",
    description="Development Server",
    variables=None,
)

servers: List[Server] = []
if STAGE == "local":
    servers.append(local_server)
if STAGE == "dev":
    servers.append(dev_server)

app.enable_swagger(
    path="/swagger",
    title="Mail delivery demo API仕様書",
    version="0.0.0",
    summary="Mail delivery demoアプリケーションのバックエンドAPIの仕様書です。",
    description=f"""

    """,
    servers=servers,
)


def lambda_handler(event: dict, context: LambdaContext) -> dict[str, str | int]:
    return app.resolve(event, context)
