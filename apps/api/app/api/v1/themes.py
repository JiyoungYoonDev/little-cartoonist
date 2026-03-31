from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.models.theme import Theme
from app.schemas.theme import ThemeResponse

router = APIRouter(prefix="/themes", tags=["themes"])


@router.get("", response_model=list[ThemeResponse])
async def list_themes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Theme).where(Theme.is_active == True))
    return result.scalars().all()
