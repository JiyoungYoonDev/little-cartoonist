from pydantic import BaseModel
from typing import Any


class MockAssistRequest(BaseModel):
    projectId: str | None = None
    teacherId: str | None = None
    theme: str | None = None


class MockAssistResponse(BaseModel):
    inferred_intent: str
    teacher_line: str
    assist_strokes: list[dict[str, Any]]
    expression: str