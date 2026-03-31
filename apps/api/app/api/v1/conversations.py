import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.models.project import Project
from app.models.conversation import Conversation
from app.schemas.conversation import ConversationCreate, ConversationResponse

router = APIRouter(prefix="/projects/{project_id}/conversations", tags=["conversations"])


@router.post("", response_model=ConversationResponse)
async def create_conversation(
    project_id: uuid.UUID,
    body: ConversationCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Project).where(Project.id == project_id))
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Project not found")

    conv = Conversation(
        project_id=project_id,
        speaker=body.speaker,
        message_text=body.message_text,
        message_type=body.message_type,
    )
    db.add(conv)
    await db.commit()
    await db.refresh(conv)
    return conv


@router.get("", response_model=list[ConversationResponse])
async def list_conversations(
    project_id: uuid.UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Conversation).where(Conversation.project_id == project_id)
    )
    return result.scalars().all()
