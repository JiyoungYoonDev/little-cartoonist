import uuid
from datetime import datetime

from pydantic import BaseModel


class StrokeCreate(BaseModel):
    stroke_type: str = "draw"
    points_json: dict
    color: str = "#000000"
    width: float = 3.0
    tool: str = "pen"
    created_by: str = "child"


class StrokeBatchCreate(BaseModel):
    strokes: list[StrokeCreate]


class StrokeResponse(BaseModel):
    id: uuid.UUID
    drawing_page_id: uuid.UUID
    stroke_type: str
    points_json: dict
    color: str
    width: float
    tool: str
    created_by: str
    created_at: datetime

    model_config = {"from_attributes": True}
