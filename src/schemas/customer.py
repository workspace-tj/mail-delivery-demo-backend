from datetime import datetime

from pydantic import Field

from src.schemas.main import BaseSchema, created_at_field, id_field, updated_at_field

email_field = Field(..., title="メールアドレス", description="ユーザーのメールアドレス", example="mail@example.com")  # type: ignore
username_field = Field(
    ..., title="ユーザー名", description="メール送信時に使用するユーザーの名前", example="山田太郎"  # type: ignore
)

class CustomerCreateRequestSchema(BaseSchema):
    email: str = email_field
    username: str = username_field

class CustomerSchema(CustomerCreateRequestSchema):
    id: str = id_field
    # created_at: datetime = created_at_field
    # updated_at: datetime = updated_at_field
