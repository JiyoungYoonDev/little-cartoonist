import uuid
from datetime import datetime

from pydantic import BaseModel


class ComicBookResponse(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    story_id: uuid.UUID
    format_type: str
    cover_image_url: str | None = None
    pdf_url: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


class ComicPageResponse(BaseModel):
    id: uuid.UUID
    page_number: int
    panel_number: int | None = None
    image_url: str
    caption_text: str | None = None
    narration_text: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
