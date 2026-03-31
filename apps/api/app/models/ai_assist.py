import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import new_uuid, utcnow


class AiAssist(Base):
    __tablename__ = "ai_assists"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    drawing_page_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("drawing_pages.id"), nullable=False)
    trigger_source: Mapped[str] = mapped_column(String(50), default="help_button")
    child_context_snapshot_json: Mapped[dict | None] = mapped_column(JSON)
    inferred_intent: Mapped[str | None] = mapped_column(String(200))
    assist_style: Mapped[str | None] = mapped_column(String(50))
    overlay_strokes_json: Mapped[dict | None] = mapped_column(JSON)
    explanation_text: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    drawing_page = relationship("DrawingPage", back_populates="ai_assists")
