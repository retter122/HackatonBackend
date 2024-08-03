from pydantic import BaseModel


class TutorialBase(BaseModel):
    pass


class TutorialCreate(TutorialBase):
    name: str
    description: str


class TutorialRead(TutorialBase):
    id: int
    name: str
    description: str


class TutorialEdit(TutorialBase):
    id: int
    name: str
    description: str