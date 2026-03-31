import uuid

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin, new_uuid


class ChildProfile(Base, TimestampMixin):
    __tablename__ = "child_profiles"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=new_uuid)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    display_name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    age_band: Mapped[str] = mapped_column(String(10), nullable=False)  # 3_5, 6_8, 9_12
    favorite_teacher_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("teacher_characters.id"))
    preferred_theme: Mapped[str | None] = mapped_column(String(100))
    avatar_url: Mapped[str | None] = mapped_column(String(500))

    user = relationship("User", back_populates="children")
    projects = relationship("Project", back_populates="child_profile")
