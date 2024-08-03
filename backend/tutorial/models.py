from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base
from ..db.annotation import intpk
from ..db.crud import CRUD


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
