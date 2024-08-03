from enum import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base
from ..db.annotation import intpk
from ..db.crud import CRUD

class TagType(str, Enum):
    backend = "BACKEND"
    frontend = "FRONTEND"
    fullstack = "FULLSTACK"
    gamedev = "GAMEDEV"
    design = "DESIGN"
    modeling3d = "MODELING3D"
    bas = "BAS"
    business = "BUSINESS"


class Tag(Base, CRUD):
    __tablename__ = 'tag'

    id: Mapped[intpk]
    tag_type: Mapped[TagType]

    source_id: Mapped[int] = mapped_column(ForeignKey("tutorial.id", ondelete="CASCADE"))

    source: Mapped['Tutorial'] = relationship(back_populates='tags', lazy="joined")