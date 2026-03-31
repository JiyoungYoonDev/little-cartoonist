import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.drawing_page import DrawingPage
from app.schemas.ai_assist import AssistRequest, AssistResponse
from app.schemas.assist import MockAssistRequest, MockAssistResponse

router = APIRouter(prefix="/assists", tags=["assist"])


@router.post("/mock", response_model=MockAssistResponse)
async def mock_assist(body: MockAssistRequest = MockAssistRequest()):
    line = "Great job! Let's draw together."

    if body.theme == "space":
        line = "Nice start! Let's add some twinkling stars together."
    elif body.theme == "animals":
        line = "I love your animal! Let's add some details."
    elif body.theme == "ocean":
        line = "Beautiful! Let's add a gentle wave together."
    elif body.theme == "fairy_tale":
        line = "What a magical scene! Let's add some sparkles."

    return MockAssistResponse(
        inferred_intent="encouragement",
        teacher_line=line,
        assist_strokes=[],
        expression="happy",
    )


@router.post("/pages/{page_id}", response_model=AssistResponse)
async def request_assist(
    page_id: uuid.UUID,
    body: AssistRequest = AssistRequest(),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(DrawingPage).where(DrawingPage.id == page_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Drawing page not found")

    # TODO: call AI pipeline service
    return AssistResponse(
        inferred_intent="placeholder",
        teacher_line="Let's draw together!",
        assist_strokes=[],
    )
