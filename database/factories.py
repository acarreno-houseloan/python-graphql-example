import factory
import factory.fuzzy
from factory.mongoengine import MongoEngineFactory

from .models import Comment as CommentModel
from .models import Post as PostModel
from .models import User as UserModel


class User(MongoEngineFactory):
    class Meta:  # type: ignore
        model = UserModel

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")


class Post(MongoEngineFactory):
    class Meta:  # type: ignore
        model = PostModel

    title = factory.Faker("sentence")
    content = factory.Faker("text")
    author = factory.fuzzy.FuzzyChoice(UserModel.objects)  # type: ignore


class Comment(MongoEngineFactory):
    class Meta:  # type: ignore
        model = CommentModel

    content = factory.Faker("text")
    author = factory.fuzzy.FuzzyChoice(UserModel.objects)  # type: ignore
    post = factory.fuzzy.FuzzyChoice(PostModel.objects)  # type: ignore
