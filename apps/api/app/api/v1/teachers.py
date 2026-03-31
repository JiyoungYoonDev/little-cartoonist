from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.teacher import TeacherCharacter
from app.schemas.teacher import TeacherResponse

router = APIRouter(prefix="/teachers", tags=["teachers"])


@router.get("", response_model=list[TeacherResponse])
async def list_teachers(db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(TeacherCharacter).where(TeacherCharacter.is_active == True)
    )
    return result.scalars().all()
