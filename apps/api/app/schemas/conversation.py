import uuid
from datetime import datetime

from pydantic import BaseModel


class ConversationCreate(BaseModel):
    speaker: str
    message_text: str
    message_type: str = "text"


class ConversationResponse(BaseModel):
    id: uuid.UUID
    project_id: uuid.UUID
    speaker: str
    message_text: str
    message_type: str
    audio_url: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}
