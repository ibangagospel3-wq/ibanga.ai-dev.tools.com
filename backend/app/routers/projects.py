from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.dependencies import get_current_user
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate,ProjectPublic,ProjectUpdate
from app.services.project_service import get_project,list_projects
router=APIRouter(prefix='/api/projects',tags=['Projects'])
@router.post('',response_model=ProjectPublic,status_code=201)
async def create(payload:ProjectCreate,db:AsyncSession=Depends(get_db),user:User=Depends(get_current_user)):
    project=Project(user_id=user.id,**payload.model_dump());db.add(project);await db.commit();await db.refresh(project);return project
@router.get('',response_model=list[ProjectPublic])
async def list_all(db=Depends(get_db),user=Depends(get_current_user)):return await list_projects(db,user.id)
@router.get('/{project_id}',response_model=ProjectPublic)
async def get(project_id:int,db=Depends(get_db),user=Depends(get_current_user)):
    project=await get_project(db,project_id,user.id)
    if not project:raise HTTPException(404,'Project not found')
    return project
@router.put('/{project_id}',response_model=ProjectPublic)
async def update(project_id:int,payload:ProjectUpdate,db=Depends(get_db),user=Depends(get_current_user)):
    project=await get_project(db,project_id,user.id)
    if not project:raise HTTPException(404,'Project not found')
    for key,value in payload.model_dump(exclude_unset=True).items():setattr(project,key,value)
    await db.commit();await db.refresh(project);return project
@router.delete('/{project_id}')
async def delete(project_id:int,db=Depends(get_db),user=Depends(get_current_user)):
    project=await get_project(db,project_id,user.id)
    if not project:raise HTTPException(404,'Project not found')
    await db.delete(project);await db.commit();return {'message':'Project deleted'}
