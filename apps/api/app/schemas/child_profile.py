import uuid
from datetime import datetime

from pydantic import BaseModel


class ChildProfileCreate(BaseModel):
    display_name: str
    age: int


class ChildProfileResponse(BaseModel):
    id: uuid.UUID
    display_name: str
    age: int
    age_band: str
    favorite_teacher_id: uuid.UUID | None = None
    avatar_url: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
