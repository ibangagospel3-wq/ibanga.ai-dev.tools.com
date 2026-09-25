from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project import Project
async def list_projects(db,user_id): return list((await db.scalars(select(Project).where(Project.user_id==user_id).order_by(Project.updated_at.desc()))).all())
async def get_project(db,project_id,user_id): return await db.scalar(select(Project).where(Project.id==project_id,Project.user_id==user_id))
