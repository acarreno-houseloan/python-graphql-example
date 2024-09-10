import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField

from .types import Comment as CommentType
from .types import Like as LikeType
from .types import Post as PostType
from .types import User as UserType


class Query(graphene.ObjectType):
    node = Node.Field()
    all_users = MongoengineConnectionField(UserType)
    all_posts = MongoengineConnectionField(PostType)
    all_comments = MongoengineConnectionField(CommentType)
    all_likes = MongoengineConnectionField(LikeType)
    user = graphene.Field(UserType, id=graphene.String())
    post = graphene.Field(PostType, id=graphene.String())
    comment = graphene.Field(CommentType, id=graphene.String())
    like = graphene.Field(LikeType, id=graphene.String())


schema = graphene.Schema(
    query=Query,
    types=[UserType, PostType, CommentType, LikeType],
)
