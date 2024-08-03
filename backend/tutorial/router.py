from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..user.auth import get_current_user
from ..user.models import User
from ..db.depencies import get_session
from ..tags.models import TagType

from .scemas import TutorialRead, TutorialCreate, TutorialEdit
from .models import Tutorial
from .relscemas import TutorialRel

router = APIRouter(prefix="/tutorial", tags=["tutorial"])


@router.delete("/{tutorial_id}")
async def delete_tutorial(tutorial_id: int, user: User = Depends(get_current_user),
                          session: AsyncSession = Depends(get_session)) -> TutorialRead:
    tutorial = await session.scalar(Tutorial.get_by_id(tutorial_id))

    if not tutorial:
        raise HTTPException(404)
    if tutorial.creator_id != user.id:
        raise HTTPException(401)

    tutorial_ret = TutorialRead.model_validate(tutorial, from_attributes=True)

    try:
        await session.delete(tutorial)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return tutorial_ret


@router.post("/")
async def create_tutorial(tutorial_new: TutorialCreate, user: User = Depends(get_current_user),
                          session: AsyncSession = Depends(get_session)) -> TutorialRead:

    tutorial = Tutorial(name=tutorial_new.name, description=tutorial_new.description,
                        creator_id=user.id)

    try:
        session.add(tutorial)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return TutorialRead.model_validate(tutorial, from_attributes=True)


@router.put("/")
async def edit_tutorial(tutorial_edit: TutorialEdit, user: User = Depends(get_current_user),
                        session: AsyncSession = Depends(get_session)) -> TutorialRead:
    tutorial = await session.scalar(Tutorial.get_by_id(tutorial_edit.id))

    if not tutorial:
        raise HTTPException(404)
    if tutorial.creator_id != user.id:
        raise HTTPException(401)

    try:
        tutorial.name = tutorial_edit.name
        tutorial.description = tutorial_edit.description

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return TutorialRead.model_validate(tutorial, from_attributes=True)


@router.get("/{tutorial_id}")
async def get_tutorial(tutorial_id: int, session: AsyncSession = Depends(get_session)) -> TutorialRel:
    tutorial = await session.scalar(Tutorial.get_by_id(tutorial_id))

    if not tutorial:
        raise HTTPException(404)

    return TutorialRel.model_validate(tutorial, from_attributes=True)


@router.get('/all/')
async def get_all_tutors(session: AsyncSession = Depends(get_session)) -> list[TutorialRel]:
    tutorials_ret = await session.scalars(Tutorial.get_all_tutorials())

    return [TutorialRel.model_validate(tutorial, from_attributes=True) for tutorial in tutorials_ret]


@router.get('/filtey/{filter}')
async def get_filter_tutors(filter: TagType, session: AsyncSession = Depends(get_session)) -> list[TutorialRel]:
    tutorials_ret = await session.scalars(Tutorial.get_filtered_tutorials(filter))

    return [TutorialRel.model_validate(tutorial, from_attributes=True) for tutorial in tutorials_ret]