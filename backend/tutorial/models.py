from sqlalchemy import ForeignKey, select, Select
from sqlalchemy.orm import Mapped, mapped_column, relationship, contains_eager

from ..db.database import Base
from ..db.annotation import intpk
from ..db.crud import CRUD
from ..tags.models import TagType, Tag


class Tutorial(Base, CRUD):
    __tablename__ = "tutorial"

    id: Mapped[intpk]

    name: Mapped[str]
    description: Mapped[str]

    creator_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'))

    creator: Mapped['User'] = relationship(back_populates='tutorials', lazy='joined')
    modules: Mapped[list['Module']] = relationship(back_populates="source", lazy="selectin",
                                                   cascade='all, delete-orphan')
    comments: Mapped[list['Comment']] = relationship(back_populates="source", lazy="selectin",
                                                     cascade="all, delete-orphan")
    tags: Mapped[list['Tag']] = relationship(back_populates="source", lazy="selectin",
                                             cascade="all, delete-orphan")

    @classmethod
    def get_all_tutorials(cls):
        query = (select(cls))
        return query

    @classmethod
    def get_filtered_tutorials(cls, filter: TagType):
        query = (select(Tutorial).join(Tutorial.tags).filter(Tag.tag_type == filter)
                 .options(contains_eager(Tutorial.tags)))
        return query