from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base
from ..db.annotation import intpk
from ..db.crud import CRUD


class Module(Base, CRUD):
    __tablename__ = 'module'

    id: Mapped[intpk]
    name: Mapped[str]
    description: Mapped[str]
    document: Mapped[str]
    source_id: Mapped[int] = mapped_column(ForeignKey("tutorial.id", ondelete="CASCADE"))

    source: Mapped['Tutorial'] = relationship(back_populates="modules", lazy='joined')
