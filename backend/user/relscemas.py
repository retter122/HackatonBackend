from .scemas import UserRead
from ..tutorial.scemas import TutorialRead
from ..comments.scemas import CommentRead

class UserRel(UserRead):
    tutorials: list[TutorialRead]
    comments: list[CommentRead]