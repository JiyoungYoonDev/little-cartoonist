import uuid
from datetime import datetime

from pydantic import BaseModel


class TeacherResponse(BaseModel):
    id: uuid.UUID
    code: str
    name: str
    animal_type: str
    personality_summary: str
    voice_style: str
    default_color_palette_json: dict | None = None

    model_config = {"from_attributes": True}


class TeacherAssetResponse(BaseModel):
    id: uuid.UUID
    asset_type: str
    asset_name: str
    asset_url: str
    metadata_json: dict | None = None

    model_config = {"from_attributes": True}
