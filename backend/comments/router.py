from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .scemas import CommentRead, CommentCreate, CommentEdit
from .model import Comment

from ..user.models import User
from ..user.auth import get_current_user
from ..db.depencies import get_session

router = APIRouter(prefix="/comment", tags=["comment"])


@router.post('/')
async def create_comment(comment_new: CommentCreate, user: User = Depends(get_current_user),
                         session: AsyncSession = Depends(get_session)) -> CommentRead:
    comment = Comment(like=comment_new.like, dislike=comment_new.dislike, text=comment_new.text,
                      source_id=comment_new.source_id, creator_id=user.id)

    try:
        session.add(comment)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return CommentRead.model_validate(comment, from_attributes=True)


@router.put('/')
async def edit_comment(comment_edit: CommentEdit, user: User = Depends(get_current_user),
                       session: AsyncSession = Depends(get_session)) -> CommentRead:
    comment = await session.scalar(Comment.get_by_id(comment_edit.id))

    if not comment:
        raise HTTPException(404)
    if comment.creator_id != user.id:
        raise HTTPException(401)

    try:
        comment.like = comment_edit.like
        comment.dislike = comment_edit.dislike

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return CommentRead.model_validate(comment, from_attributes=True)


@router.delete('/{comment_id}')
async def delete_comment(comment_id: int, user: User = Depends(get_current_user),
                         session: AsyncSession = Depends(get_session)) -> CommentRead:
    comment = await session.scalar(Comment.get_by_id(comment_id))

    if not comment:
        raise HTTPException(404)
    if comment.creator_id != user.id:
        raise HTTPException(401)

    comment_ret = CommentRead.model_validate(comment, from_attributes=True)

    try:
        await session.delete(comment)

        await session.commit()
    except Exception as e:
        raise HTTPException(403)

    return comment_ret