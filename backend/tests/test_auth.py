import pytest
from app.services.auth_service import register_user
@pytest.mark.asyncio
async def test_password_policy_rejects_weak_password():
    with pytest.raises(Exception):
        from app.utils.validators import validate_password
        validate_password('weak')
