from datetime import datetime
from sqlalchemy import DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
class Challenge(Base):
    __tablename__ = "challenges"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(160))
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(30), index=True)
    difficulty: Mapped[str] = mapped_column(String(30), default="Beginner")
    starter_html: Mapped[str] = mapped_column(Text, default="")
    starter_css: Mapped[str] = mapped_column(Text, default="")
    starter_javascript: Mapped[str] = mapped_column(Text, default="")
    expected_behavior: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
