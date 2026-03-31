from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.child_profile import ChildProfile
from app.schemas.child_profile import ChildProfileCreate, ChildProfileResponse

router = APIRouter(prefix="/children", tags=["children"])


def compute_age_band(age: int) -> str:
    if age <= 5:
        return "3_5"
    elif age <= 8:
        return "6_8"
    return "9_12"


@router.post("", response_model=ChildProfileResponse)
async def create_child(
    body: ChildProfileCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    child = ChildProfile(
        user_id=user.id,
        display_name=body.display_name,
        age=body.age,
        age_band=compute_age_band(body.age),
    )
    db.add(child)
    await db.commit()
    await db.refresh(child)
    return child


@router.get("", response_model=list[ChildProfileResponse])
async def list_children(
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(ChildProfile).where(ChildProfile.user_id == user.id)
    )
    return result.scalars().all()
