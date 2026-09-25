from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
class Lesson(Base):
    __tablename__ = "lessons"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(160))
    slug: Mapped[str] = mapped_column(String(180), unique=True, index=True)
    category: Mapped[str] = mapped_column(String(30), index=True)
    description: Mapped[str] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    difficulty: Mapped[str] = mapped_column(String(30), default="Beginner")
    order_number: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
