from fastapi import APIRouter,Depends,Query,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import get_current_user
from app.models.lesson import Lesson
from app.models.user import User
from app.schemas.lesson import LessonPublic
router=APIRouter(prefix='/api/lessons',tags=['Lessons'])
@router.get('',response_model=list[LessonPublic])
async def lessons(category:str|None=Query(None),difficulty:str|None=Query(None),db:AsyncSession=Depends(get_db)):
    query=select(Lesson).order_by(Lesson.category,Lesson.order_number)
    if category:query=query.where(Lesson.category.ilike(category))
    if difficulty:query=query.where(Lesson.difficulty.ilike(difficulty))
    return list((await db.scalars(query)).all())
@router.get('/category/{category}',response_model=list[LessonPublic])
async def by_category(category:str,db:AsyncSession=Depends(get_db)):return list((await db.scalars(select(Lesson).where(Lesson.category.ilike(category)).order_by(Lesson.order_number))).all())
@router.get('/{lesson_id}',response_model=LessonPublic)
async def lesson(lesson_id:int,db:AsyncSession=Depends(get_db)):
    item=await db.get(Lesson,lesson_id)
    if not item:raise HTTPException(404,'Lesson not found')
    return item
