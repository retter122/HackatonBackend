from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserRegister(UserBase):
    name: str
    password: str
    mail: str


class UserAuthtorize(UserBase):
    password: str
    mail: str


class UserEdit(UserBase):
    description: str


class UserRead(UserBase):
    id: int

    name: str
    mail: str
    description: str