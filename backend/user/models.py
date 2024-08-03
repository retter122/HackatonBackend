from ..db.database import Base
from ..db.crud import CRUD
from ..db.annotation import intpk

from sqlalchemy import ForeignKey, select, Select
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base, CRUD):
    __tablename__ = 'user'

    id: Mapped[intpk]

    name: Mapped[str]
    password: Mapped[str]
    mail: Mapped[str]

    tutorials: Mapped[list['Tutorial']] = relationship(back_populates='creator', lazy='selectin',
                                                       cascade='all, delete-orphan')
    comments: Mapped[list['Comment']] = relationship(back_populates='creator', lazy='selectin',
                                                     cascade='all, delete-orphan')

    @classmethod
    def get_by_mail(cls, mail: str):
        query = (select(cls).where(cls.mail == mail))
        return query
