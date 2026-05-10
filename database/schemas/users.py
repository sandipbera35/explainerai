from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from datetime import datetime

from database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    guid : Mapped[str] =mapped_column(String(255), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(255))
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    profile_picture: Mapped[str] = mapped_column(String(255), nullable=True)
    profile_cover: Mapped[str] = mapped_column(String(255), nullable=True)
    bio: Mapped[str] = mapped_column(String(255), nullable=True)
    location: Mapped[str] = mapped_column(String(255), nullable=True)
    website: Mapped[str] = mapped_column(String(255), nullable=True)
    twitter: Mapped[str] = mapped_column(String(255), nullable=True)
    github: Mapped[str] = mapped_column(String(255), nullable=True)
    linkedin: Mapped[str] = mapped_column(String(255), nullable=True)
    instagram: Mapped[str] = mapped_column(String(255), nullable=True)
    facebook: Mapped[str] = mapped_column(String(255), nullable=True)