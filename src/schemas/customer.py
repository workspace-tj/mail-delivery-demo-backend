from datetime import datetime

from pydantic import Field

from schemas.index import id_field, created_at_field, updated_at_field, BaseSchema

email_field = Field(..., title="メールアドレス", description="ユーザーのメールアドレス", example="mail@example.com") # type: ignore
username_field = Field(
        ..., title="ユーザー名", description="メール送信時に使用するユーザーの名前", example="山田太郎" # type: ignore
    )

class CustomerSchema(BaseSchema):
    id: str = id_field
    email: str = email_field
    username: str = username_field
    created_at: datetime = created_at_field
    updated_at: datetime = updated_at_field
