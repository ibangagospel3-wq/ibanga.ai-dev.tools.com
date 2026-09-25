from datetime import datetime, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.utils.security import create_access_token, hash_password, verify_password
from app.utils.validators import normalize_email, validate_password
async def register_user(db: AsyncSession, full_name: str, email: str, password: str) -> User:
    email=normalize_email(email);validate_password(password)
    if await db.scalar(select(User).where(User.email==email)): raise ValueError("An account with this email already exists")
    user=User(full_name=full_name.strip(),email=email,password_hash=hash_password(password));db.add(user);await db.commit();await db.refresh(user);return user
async def authenticate_user(db: AsyncSession,email: str,password: str) -> User|None:
    user=await db.scalar(select(User).where(User.email==normalize_email(email)))
    if not user or not verify_password(password,user.password_hash): return None
    user.last_login=datetime.now(timezone.utc);await db.commit();await db.refresh(user);return user
def token_for_user(user: User)->str:return create_access_token(str(user.id))
