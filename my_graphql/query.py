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
    users = graphene.List(
        UserType,
        id=graphene.Int(),
        username=graphene.String(),
        email=graphene.String(),
        created_at=graphene.String(),
    )
    posts = graphene.List(PostType, id=graphene.Int())
    comments = graphene.List(CommentType, id=graphene.Int())
    likes = graphene.List(LikeType, id=graphene.Int())

    def resolve_users(self, _info, **kwargs):
        query = {}
        if "id" in kwargs:
            query["id"] = kwargs.pop("id")
        if "username" in kwargs:
            query["username"] = kwargs.pop("username")
        if "email" in kwargs:
            query["email"] = kwargs.pop("email")
        return list(UserModel.objects(**query).all())  # type: ignore

    def resolve_posts(self, _info, **kwargs):
        query = {}
        if "id" in kwargs:
            query["id"] = kwargs.pop("id")
        return list(PostModel.objects(**kwargs).all())  # type: ignore

    def resolve_comments(self, _info, **kwargs):
        query = {}
        if "id" in kwargs:
            query["id"] = kwargs.pop("id")
        return list(CommentModel.objects(**kwargs).all())  # type: ignore

    def resolve_likes(self, _info, **kwargs):
        query = {}
        if "id" in kwargs:
            query["id"] = kwargs.pop("id")
        return list(LikeModel.objects(**kwargs).all())  # type: ignore
