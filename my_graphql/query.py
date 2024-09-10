import graphene
from graphene.relay import Node

from database.models import Comment as CommentModel
from database.models import Like as LikeModel
from database.models import Post as PostModel
from database.models import User as UserModel

from .types import Comment as CommentType
from .types import Like as LikeType
from .types import Post as PostType
from .types import User as UserType


class Query(graphene.ObjectType):
    node = Node.Field()
    users = graphene.List(UserType)
    posts = graphene.List(PostType)
    comments = graphene.List(CommentType)
    likes = graphene.List(LikeType)

    def resolve_users(self, _info):
        return list(UserModel.objects.all())  # type: ignore

    def resolve_posts(self, _info):
        return list(PostModel.objects.all())  # type: ignore

    def resolve_comments(self, _info):
        return list(CommentModel.objects.all())  # type: ignore

    def resolve_likes(self, _info):
        return list(LikeModel.objects.all())  # type: ignore
