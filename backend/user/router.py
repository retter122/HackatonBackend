import base64

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends

from .scemas import UserRegister, UserAuthtorize, UserEdit, UserRead
from .models import User
from .auth import get_current_user
from .relscemas import UserRel

from ..db.depencies import get_session

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/registration/")
async def register_user(user_reg: UserRegister, session: AsyncSession = Depends(get_session)) -> dict:
    if await session.scalar(User.get_by_mail(user_reg.mail)):
        raise HTTPException(401)

    user = User(name=user_reg.name, password=user_reg.password, mail=user_reg.mail, description="")

    try:
        session.add(user)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return { 'token': base64.b64encode(str(user.id).encode()).decode() }


@router.post("/login/")
async def login_user(user_log: UserAuthtorize, session: AsyncSession = Depends(get_session)) -> dict:
    user = await session.scalar(User.get_by_mail(user_log.mail))

    if not user:
        raise HTTPException(404)
    if user.password != user_log.password:
        raise HTTPException(401)

    return { 'token': base64.b64encode(str(user.id).encode()).decode() }


@router.put('/')
async def add_descrtiption(user_edit: UserEdit, user: User = Depends(get_current_user),
                           session: AsyncSession = Depends(get_session)) -> UserRead:
    try:
        user.description = user_edit.description
        user.name = user_edit.name

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return UserRead.model_validate(user, from_attributes=True)


@router.get("/")
async def get_user(user: User = Depends(get_current_user), session: AsyncSession = Depends(get_session)) -> UserRel:
    return UserRel.model_validate(user, from_attributes=True)
