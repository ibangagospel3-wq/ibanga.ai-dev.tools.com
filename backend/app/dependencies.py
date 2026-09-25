from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User
from app.utils.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")
async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> User:
    credentials_error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    try:
        payload = decode_token(token)
        user_id = int(payload.get("sub", ""))
    except (JWTError, ValueError, TypeError):
        raise credentials_error
    user = await db.scalar(select(User).where(User.id == user_id))
    if not user or not user.is_active:
        raise credentials_error
    return user
