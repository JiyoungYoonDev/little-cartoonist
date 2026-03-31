import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import new_uuid, utcnow


class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    speaker: Mapped[str] = mapped_column(String(20), nullable=False)  # child, teacher, system
    message_text: Mapped[str] = mapped_column(String(2000), nullable=False)
    message_type: Mapped[str] = mapped_column(String(30), default="text")  # spoken, text, generated_prompt, correction, praise
    audio_url: Mapped[str | None] = mapped_column(String(500))
    metadata_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    project = relationship("Project", back_populates="conversations")
