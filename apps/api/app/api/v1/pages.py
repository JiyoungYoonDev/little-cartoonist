import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.project import Project
from app.models.drawing_page import DrawingPage
from app.schemas.drawing_page import DrawingPageResponse

router = APIRouter(prefix="/projects/{project_id}/pages", tags=["pages"])


@router.post("", response_model=DrawingPageResponse)
async def create_page(
    project_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # determine next page number
    pages_result = await db.execute(
        select(DrawingPage).where(DrawingPage.project_id == project_id)
    )
    existing_pages = pages_result.scalars().all()
    next_number = len(existing_pages) + 1

    page = DrawingPage(project_id=project_id, page_number=next_number)
    db.add(page)
    await db.commit()
    await db.refresh(page)
    return page
