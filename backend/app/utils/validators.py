import re
from fastapi import HTTPException, status

def normalize_email(email: str) -> str:
    return email.strip().lower()

def validate_password(password: str) -> str:
    if len(password) < 8:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Password must be at least 8 characters.")
    if not re.search(r"[A-Za-z]", password) or not re.search(r"\d", password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Password must contain letters and numbers.")
    return password
