from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .scemas import TagCreate, TagRead
from .models import Tag, TagType

from ..db.depencies import get_session
from ..user.models import User
from ..user.auth import get_current_user
from ..tutorial.models import Tutorial

router = APIRouter(prefix="/tags", tags=["tags"])


@router.post('/')
async def create_tag(tag_new: TagCreate, user: User = Depends(get_current_user),
                     session: AsyncSession = Depends(get_session)) -> TagRead:
    tutorial = await session.scalar(Tutorial.get_by_id(tag_new.source_id))

    if not tutorial:
        raise HTTPException(404)
    if tutorial.creator_id != user.id:
        raise HTTPException(401)

    tag = Tag(source_id=tag_new.source_id, tag_type=tag_new.tag_type)

    try:
        session.add(tag)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return TagRead.model_validate(tag, from_attributes=True)


@router.delete('/{tag_id}')
async def delete_tag(tag_id: int, user: User = Depends(get_current_user),
                     session: AsyncSession = Depends(get_session)) -> TagRead:
    tag = await session.scalar(Tag.get_by_id(tag_id))

    if not tag:
        raise HTTPException(404)
    if tag.source.creator_id != user.id:
        raise HTTPException(401)

    tag_ret = TagRead.model_validate(tag, from_attributes=True)

    try:
        await session.delete(tag)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return tag_ret
