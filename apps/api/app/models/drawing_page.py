import uuid

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, new_uuid


class DrawingPage(Base, TimestampMixin):
    __tablename__ = "drawing_pages"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    page_number: Mapped[int] = mapped_column(Integer, default=1)
    background_color: Mapped[str] = mapped_column(String(20), default="#FFFFFF")
    snapshot_image_url: Mapped[str | None] = mapped_column(String(500))
    recognized_scene_summary: Mapped[str | None] = mapped_column(String(1000))

    project = relationship("Project", back_populates="pages")
    strokes = relationship("Stroke", back_populates="drawing_page")
    ai_assists = relationship("AiAssist", back_populates="drawing_page")
