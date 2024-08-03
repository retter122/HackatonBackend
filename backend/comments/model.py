from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ..db.crud import CRUD
from ..db.annotation import intpk
from ..db.database import Base


class Comment(CRUD, Base):
    __tablename__ = 'comment'

    id: Mapped[intpk]

    like: Mapped[bool]
    dislike: Mapped[bool]
    text: Mapped[str]

    creator_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    source_id: Mapped[int] = mapped_column(ForeignKey("tutorial.id", ondelete="CASCADE"))

    creator: Mapped['User'] = relationship(back_populates='comments', lazy='joined')
    source: Mapped['Tutorial'] = relationship(back_populates='comments', lazy='joined')
