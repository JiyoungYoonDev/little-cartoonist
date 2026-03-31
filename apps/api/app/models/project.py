import uuid
from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, new_uuid


class Project(Base, TimestampMixin):
    __tablename__ = "projects"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    child_profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("child_profiles.id"), nullable=False)
    teacher_character_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teacher_characters.id"), nullable=False)
    theme_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("themes.id"))
    title: Mapped[str] = mapped_column(String(200), default="Untitled")
    status: Mapped[str] = mapped_column(String(50), default="draft")  # draft, in_progress, story_ready, comic_ready, archived
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    child_profile = relationship("ChildProfile", back_populates="projects")
    pages = relationship("DrawingPage", back_populates="project")
    conversations = relationship("Conversation", back_populates="project")
    stories = relationship("Story", back_populates="project")
    comic_books = relationship("ComicBook", back_populates="project")
