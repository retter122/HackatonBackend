from pydantic import BaseModel


class CommentBase(BaseModel):
    pass


class CommentCreate(CommentBase):
    source_id: int

    like: int
    dislike: int
    text: str


class CommentRead(CommentBase):
    id: int

    like: bool
    dislike: bool
    text: str


class CommentEdit(CommentBase):
    id: int

    like: bool
    dislike: bool
