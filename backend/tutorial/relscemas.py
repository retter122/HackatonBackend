from .scemas import TutorialRead

from ..modules.scemas import ModuleRead
from ..comments.scemas import CommentRead
from ..tags.scemas import TagRead


class TutorialRel(TutorialRead):
    modules: list[ModuleRead]
    comments: list[CommentRead]
    tags: list[TagRead]
