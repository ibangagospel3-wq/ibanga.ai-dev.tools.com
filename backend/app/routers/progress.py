from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import get_current_user
from app.models.lesson import Lesson
from app.models.progress import Progress
from app.models.user import User
from app.schemas.progress import ProgressPublic
from app.services.progress_service import complete_lesson
router=APIRouter(prefix='/api/progress',tags=['Progress'])
@router.get('',response_model=list[ProgressPublic])
async def progress(db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):return list((await db.scalars(select(Progress).where(Progress.user_id==user.id))).all())
@router.post('/{lesson_id}/complete',response_model=ProgressPublic)
async def complete(lesson_id:int,db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):
    if not await db.get(Lesson,lesson_id):raise HTTPException(404,'Lesson not found')
    return await complete_lesson(db,user.id,lesson_id)
