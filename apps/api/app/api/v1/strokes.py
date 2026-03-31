import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.drawing_page import DrawingPage
from app.models.stroke import Stroke
from app.schemas.stroke import StrokeBatchCreate, StrokeResponse

router = APIRouter(prefix="/pages/{page_id}/strokes", tags=["strokes"])


@router.post("/batch", response_model=list[StrokeResponse])
async def create_strokes_batch(
    page_id: uuid.UUID,
    body: StrokeBatchCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(DrawingPage).where(DrawingPage.id == page_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Drawing page not found")

    created = []
    for s in body.strokes:
        stroke = Stroke(
            drawing_page_id=page_id,
            stroke_type=s.stroke_type,
            points_json=s.points_json,
            color=s.color,
            width=s.width,
            tool=s.tool,
            created_by=s.created_by,
        )
        db.add(stroke)
        created.append(stroke)

    await db.commit()
    for stroke in created:
        await db.refresh(stroke)
    return created
