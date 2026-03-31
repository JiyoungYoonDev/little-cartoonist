import uuid
from datetime import datetime

from pydantic import BaseModel


class ProjectCreate(BaseModel):
    child_profile_id: uuid.UUID
    teacher_character_id: uuid.UUID
    theme_id: uuid.UUID | None = None


class ProjectResponse(BaseModel):
    id: uuid.UUID
    child_profile_id: uuid.UUID
    teacher_character_id: uuid.UUID
    theme_id: uuid.UUID | None = None
    title: str
    status: str
    started_at: datetime | None = None
    completed_at: datetime | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
