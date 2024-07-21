from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.event_handler.api_gateway import Router

from controllers.email_request import EmailRequestController
from schemas import errors
from schemas.main import MessageSchema

app = APIGatewayRestResolver(debug=True)
router = Router()

controller = EmailRequestController()


@router.post(
    "/all",
    tags=["EmailRequest"],
    summary="emailの一斉送信リクエスト",
    description="""
## 概要

DBに保管されているカスタマーデータのすべてのメールアドレスに
メールを一斉送信するリクエストをキューに入れるエンドポイントです。

## 変更履歴

""",
    response_description="一斉送信リクエストをキューに送信完了",
    operation_id="postEmailRequestAll",
    responses={
        200: {"description": "一斉送信リクエストをキューに送信完了"},
        400: errors.BAD_REQUEST_ERROR,
        401: errors.UNAUTHORIZED_ERROR,
        404: errors.NOT_FOUND_ERROR,
        500: errors.INTERNAL_SERVER_ERROR,
    },
)
def queue_email_requests_to_customer_all() -> MessageSchema:
    return controller.queue_email_requests_to_customer_all()  # type: ignore
