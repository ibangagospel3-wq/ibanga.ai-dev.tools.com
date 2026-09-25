from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import get_current_user
from app.models.notification import Notification
from app.models.user import User
from app.schemas.notification import NotificationPublic
router=APIRouter(prefix='/api/notifications',tags=['Notifications'])
@router.get('',response_model=list[NotificationPublic])
async def notifications(db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):return list((await db.scalars(select(Notification).where(Notification.user_id==user.id).order_by(Notification.created_at.desc()))).all())
@router.put('/{notification_id}/read',response_model=NotificationPublic)
async def mark_read(notification_id:int,db=Depends(get_db),user=Depends(get_current_user)):
    item=await db.scalar(select(Notification).where(Notification.id==notification_id,Notification.user_id==user.id))
    if not item:raise HTTPException(404,'Notification not found')
    item.is_read=True;await db.commit();await db.refresh(item);return item
