import graphene
from graphene import relay
from graphene_mongo import MongoengineObjectType

from database.models import CommentModel as CommentModel
from database.models import LikeModel as LikeModel
from database.models import PostModel as PostModel
from database.models import UserModel as UserModel


class UserType(MongoengineObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)

    username = graphene.String()


class PostType(MongoengineObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node,)
        exclude_fields = ("author_id",)


class CommentType(MongoengineObjectType):
    class Meta:
        model = CommentModel
        interfaces = (relay.Node,)
        exclude_fields = ("author_id", "post_id")


class LikeType(MongoengineObjectType):
    class Meta:
        model = LikeModel
        interfaces = (relay.Node,)
        exclude_fields = ("user_id", "post_id")
