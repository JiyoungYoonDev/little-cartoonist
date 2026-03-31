import uuid
from datetime import datetime

from sqlalchemy import String, Boolean, JSON, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, new_uuid, utcnow


class TeacherCharacter(Base, TimestampMixin):
    __tablename__ = "teacher_characters"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    animal_type: Mapped[str] = mapped_column(String(50), nullable=False)
    personality_summary: Mapped[str] = mapped_column(String(500), nullable=False)
    voice_style: Mapped[str] = mapped_column(String(100), nullable=False)
    default_color_palette_json: Mapped[dict | None] = mapped_column(JSON)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    assets = relationship("TeacherAsset", back_populates="teacher_character")


class TeacherAsset(Base):
    __tablename__ = "teacher_assets"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    teacher_character_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("teacher_characters.id"), nullable=False)
    asset_type: Mapped[str] = mapped_column(String(50), nullable=False)
    asset_name: Mapped[str] = mapped_column(String(100), nullable=False)
    asset_url: Mapped[str] = mapped_column(String(500), nullable=False)
    metadata_json: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)

    teacher_character = relationship("TeacherCharacter", back_populates="assets")
