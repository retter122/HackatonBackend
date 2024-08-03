import base64
from fastapi import Depends, Security, HTTPException
from fastapi.security import APIKeyHeader

from sqlalchemy.ext.asyncio import AsyncSession

from ..db.depencies import get_session
from .models import User

api_key = APIKeyHeader(name='Authorization')


async def get_current_user(token: str = Security(api_key), session: AsyncSession = Depends(get_session)) -> User:
    user_id = int(base64.b64decode(token))

    user = await session.scalar(User.get_by_id(user_id))

    if not user:
        raise HTTPException(401)

    return user
