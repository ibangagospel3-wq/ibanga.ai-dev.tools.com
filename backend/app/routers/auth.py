from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest, UserPublic
from app.services.auth_service import authenticate_user, register_user, token_for_user


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register", response_model=UserPublic, status_code=201)
async def register(
    payload: RegisterRequest,
    db: AsyncSession = Depends(get_db)
):
    try:
        return await register_user(
            db,
            payload.full_name,
            payload.email,
            payload.password
        )
    except ValueError as exc:
        raise HTTPException(409, str(exc))
    except (SQLAlchemyError, OSError) as exc:
        raise HTTPException(
            503,
            "Database unavailable. Start PostgreSQL and verify DATABASE_URL."
        ) from exc


@router.post("/login", response_model=AuthResponse)
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(
        db,
        payload.email,
        payload.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    return {
        "access_token": token_for_user(user),
        "user": user
    }


@router.post("/token")
async def swagger_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    return {
        "access_token": token_for_user(user),
        "token_type": "bearer"
    }


@router.get("/me", response_model=UserPublic)
async def me(
    user: User = Depends(get_current_user)
):
    return user


@router.post("/logout")
async def logout(
    user: User = Depends(get_current_user)
):
    return {
        "message": "Logged out. Delete the bearer token on the client."
    }