import graphene
from graphene_mongo import MongoengineObjectType

from database.models import Comment as CommentModel
from database.models import Like as LikeModel
from database.models import Post as PostModel
from database.models import User as UserModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel


class Post(MongoengineObjectType):
    class Meta:
        model = PostModel

    author = graphene.Field(User)


class Comment(MongoengineObjectType):
    class Meta:
        model = CommentModel

    author = graphene.Field(User)
    post = graphene.Field(Post)


class Like(MongoengineObjectType):
    class Meta:
        model = LikeModel

    user = graphene.Field(User)
