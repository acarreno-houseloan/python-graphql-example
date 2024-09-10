import graphene
from graphene import relay
from graphene_mongo import MongoengineObjectType

from database.models import Comment as CommentModel
from database.models import Like as LikeModel
from database.models import Post as PostModel
from database.models import User as UserModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)

    username = graphene.String()


class Post(MongoengineObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node,)
        exclude_fields = ("author_id",)


class Comment(MongoengineObjectType):
    class Meta:
        model = CommentModel
        interfaces = (relay.Node,)
        exclude_fields = ("author_id", "post_id")


class Like(MongoengineObjectType):
    class Meta:
        model = LikeModel
        interfaces = (relay.Node,)
        exclude_fields = ("user_id", "post_id")
