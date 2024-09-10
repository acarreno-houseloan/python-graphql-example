import graphene

from .query import Query
from .types import Comment as CommentType
from .types import Like as LikeType
from .types import Post as PostType
from .types import User as UserType

schema = graphene.Schema(
    query=Query,
    types=[UserType, PostType, CommentType, LikeType],
)
