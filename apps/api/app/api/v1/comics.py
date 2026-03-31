import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.project import Project
from app.schemas.comic import ComicBookResponse

router = APIRouter(prefix="/projects/{project_id}", tags=["comics"])


@router.post("/generate-comic", response_model=ComicBookResponse)
async def generate_comic(
    project_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    # TODO: call AI pipeline comic generation service
    raise HTTPException(status_code=501, detail="Comic generation not yet implemented")
