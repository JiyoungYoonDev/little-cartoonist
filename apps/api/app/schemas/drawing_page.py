import uuid
from datetime import datetime

from pydantic import BaseModel


class DrawingPageResponse(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    page_number: int
    background_color: str
    snapshot_image_url: str | None = None
    recognized_scene_summary: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
