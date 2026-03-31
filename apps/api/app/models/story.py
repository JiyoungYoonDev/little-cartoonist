import uuid

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, new_uuid


class Story(Base, TimestampMixin):
    __tablename__ = "stories"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    story_text: Mapped[str] = mapped_column(Text, nullable=False)
    narration_text: Mapped[str | None] = mapped_column(Text)
    age_band: Mapped[str | None] = mapped_column(String(10))
    generated_by_model: Mapped[str | None] = mapped_column(String(100))

    project = relationship("Project", back_populates="stories")
    comic_books = relationship("ComicBook", back_populates="story")
