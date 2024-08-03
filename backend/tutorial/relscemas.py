from .scemas import TutorialRead
from ..modules.scemas import ModuleRead
from ..comments.scemas import CommentRead


class TutorialRel(TutorialRead):
    modules: list[ModuleRead]
    comments: list[CommentRead]
