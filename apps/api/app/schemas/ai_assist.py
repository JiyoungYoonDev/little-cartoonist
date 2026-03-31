import uuid
from datetime import datetime

from pydantic import BaseModel


class AiAssistResponse(BaseModel):
    id: uuid.UUID
    inferred_intent: str | None = None
    assist_style: str | None = None
    overlay_strokes_json: dict | None = None
    explanation_text: str | None = None
    created_at: datetime

    model_config = {"from_attributes": True}


class AssistRequest(BaseModel):
    trigger_source: str = "help_button"


class AssistResponse(BaseModel):
    inferred_intent: str | None = None
    teacher_line: str
    assist_strokes: list[dict] = []
