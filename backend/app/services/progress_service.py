from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.progress import Progress
async def complete_lesson(db:AsyncSession,user_id:int,lesson_id:int)->Progress:
    progress=await db.scalar(select(Progress).where(Progress.user_id==user_id,Progress.lesson_id==lesson_id))
    if not progress: progress=Progress(user_id=user_id,lesson_id=lesson_id);db.add(progress)
    progress.completed=True;progress.completed_at=datetime.now(timezone.utc);await db.commit();await db.refresh(progress);return progress
