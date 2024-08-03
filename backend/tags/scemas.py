from pydantic import BaseModel
from .models import TagType


class TagBase(BaseModel):
    pass


class TagCreate(TagBase):
    source_id: int

    tag_type: TagType


class TagRead(TagBase):
    id: int

    tag_type: TagType
