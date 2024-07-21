from datetime import datetime

from pydantic import Field, BaseModel
from pydantic.alias_generators import to_camel

id_field = Field(
    ...,
    title="データのID",
    description="データのID(uuidのハイフン無し)",
    # uuid without hyphen
    example="00000000000000000000000000000000",  # type: ignore
)

created_at_field = Field(
    ..., title="作成日時", description="データが作成された日時", example=datetime.now().isoformat()  # type: ignore
)   


updated_at_field = Field(
    ..., title="更新日時", description="データが最後に更新された日時", example=datetime.now().isoformat()  # type: ignore
)

class BaseSchema(BaseModel):
    class Config:
        alias_generator = to_camel
        