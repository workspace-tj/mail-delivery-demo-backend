from enum import Enum

from pydantic import Field

from src.schemas.main import BaseSchema


class EmailType(str, Enum):
    REGISTER = "EMAIL_TYPE_REGISTER"
    PASSWORDRESET = "EMAIL_TYPE_PASSWORDRESET"
    CONFIRMATION = "EMAIL_TYPE_CONFIRMATION"
    NOTIFICATION = "EMAIL_TYPE_NOTIFICATION"
    APPLOGIZE = "EMAIL_TYPE_APPLOGIZE"
    COMERCIAL = "EMAIL_TYPE_COMERCIAL"
    MARKETPLACE = "EMAIL_TYPE_MARKETPLACE"
    TICKET = "EMAIL_TYPE_TICKET"
    INVITE = "EMAIL_TYPE_INVITE"
    PAYMENT = "EMAIL_TYPE_PAYMENT"
    OTHER = "EMAIL_TYPE_OTHER"


email_type_field = Field(..., title="メール種別", description="メール種別(e.g., 新規登録, パスワードリセット)", example="EMAIL_TYPE_REGISTER")  # type: ignore
subject_field = Field(..., title="件名", description="メールの件名", example="新規サービスのご紹介")  # type: ignore
text_field = Field(..., title="メール本文（プレーンテキスト）", description="プレーンテキストメールの本文", example="${username} 様\n 日頃よりお世話になっております。株式会社...")  # type: ignore
html_text_field = Field(..., title="メール本文（html）", description="HTMLメールの本文", example="<!DOCTYPE html><html><head>...")  # type: ignore
# TODO: 一斉送信メールのメールテキストをs3に保管し、その内容を送信する
# object_key_field =


class EmailRequestSchema(BaseSchema):
    email_type: EmailType = email_type_field
    subject: str = subject_field
    text: str = text_field
    html_text: str = html_text_field
