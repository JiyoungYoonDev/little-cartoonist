import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.project import Project
from app.schemas.story import StoryResponse

router = APIRouter(prefix="/projects/{project_id}", tags=["stories"])


@router.post("/generate-story", response_model=StoryResponse)
async def generate_story(
    project_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # TODO: call AI pipeline story generation service
    from app.models.story import Story
    story = Story(
        project_id=project_id,
        title="My Story",
        story_text="Once upon a time...",
        age_band="3_5",
        generated_by_model="placeholder",
    )
    db.add(story)
    await db.commit()
    await db.refresh(story)
    return story
