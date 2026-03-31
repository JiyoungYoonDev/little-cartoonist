import uuid

from pydantic import BaseModel


class ThemeResponse(BaseModel):
    id: uuid.UUID
    code: str
    name: str
    description: str | None = None
    age_min: int
    age_max: int

    model_config = {"from_attributes": True}
