from .scemas import TutorialRead
from ..modules.scemas import ModuleRead


class TutorialRel(TutorialRead):
    modules: list[ModuleRead]
