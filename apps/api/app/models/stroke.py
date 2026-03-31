import uuid
from datetime import datetime

from sqlalchemy import String, Float, ForeignKey, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import new_uuid, utcnow


class Stroke(Base):
    __tablename__ = "strokes"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    drawing_page_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("drawing_pages.id"), nullable=False)
    stroke_type: Mapped[str] = mapped_column(String(20), default="draw")
    points_json: Mapped[dict] = mapped_column(JSON, nullable=False)
    color: Mapped[str] = mapped_column(String(20), default="#000000")
    width: Mapped[float] = mapped_column(Float, default=3.0)
    tool: Mapped[str] = mapped_column(String(20), default="pen")
    created_by: Mapped[str] = mapped_column(String(10), default="child")  # child, ai
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    drawing_page = relationship("DrawingPage", back_populates="strokes")
