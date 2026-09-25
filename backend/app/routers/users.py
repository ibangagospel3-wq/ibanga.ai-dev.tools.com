from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.auth import UserPublic
from app.schemas.user import UserUpdate
router=APIRouter(prefix='/api/users',tags=['Users'])
@router.get('/me',response_model=UserPublic)
async def get_me(user:User=Depends(get_current_user)):return user
@router.put('/me',response_model=UserPublic)
async def update_me(payload:UserUpdate,db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):
    for key,value in payload.model_dump(exclude_unset=True).items():setattr(user,key,value.strip() if isinstance(value,str) else value)
    await db.commit();await db.refresh(user);return user
