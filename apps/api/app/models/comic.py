import uuid
from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, new_uuid, utcnow


class ComicBook(Base, TimestampMixin):
    __tablename__ = "comic_books"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), nullable=False)
    story_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("stories.id"), nullable=False)
    format_type: Mapped[str] = mapped_column(String(50), default="comic_4_panel")
    cover_image_url: Mapped[str | None] = mapped_column(String(500))
    pdf_url: Mapped[str | None] = mapped_column(String(500))

    project = relationship("Project", back_populates="comic_books")
    story = relationship("Story", back_populates="comic_books")
    pages = relationship("ComicPage", back_populates="comic_book")


class ComicPage(Base):
    __tablename__ = "comic_pages"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    comic_book_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("comic_books.id"), nullable=False)
    page_number: Mapped[int] = mapped_column(Integer, nullable=False)
    panel_number: Mapped[int | None] = mapped_column(Integer)
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)
    caption_text: Mapped[str | None] = mapped_column(String(500))
    narration_text: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    comic_book = relationship("ComicBook", back_populates="pages")
