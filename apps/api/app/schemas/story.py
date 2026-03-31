import uuid
from datetime import datetime

from pydantic import BaseModel


class StoryResponse(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    title: str
    story_text: str
    narration_text: str | None = None
    age_band: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
