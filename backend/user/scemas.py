from pydantic import BaseModel
from ..tutorial.scemas import TutorialRead


class UserBase(BaseModel):
    pass


class UserRegister(UserBase):
    name: str
    password: str
    mail: str


class UserAuthtorize(UserBase):
    password: str
    mail: str


class UserRead(UserBase):
    id: int
    name: str
    mail: str

    tutorials: list[TutorialRead]