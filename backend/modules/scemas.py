from pydantic import BaseModel


class ModuleBase(BaseModel):
    pass


class ModuleCreate(ModuleBase):
    name: str
    description: str
    source_id: int


class ModuleRead(ModuleBase):
    id: int
    name: str
    description: str
    document: str


class ModuleEdit(ModuleBase):
    id: int
    name: str
    description: str