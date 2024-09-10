from datetime import datetime

from mongoengine import Document
from mongoengine.fields import DateTimeField
from mongoengine.fields import ObjectIdField
from mongoengine.fields import ReferenceField
from mongoengine.fields import StringField


class UserModel(Document):
    meta = {"collection": "users"}

    username = StringField()
    email = StringField()
    password = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def __repr__(self):
        return self.username


class PostModel(Document):
    meta = {"collection": "posts"}

    author = ReferenceField(UserModel)
    title = StringField()
    content = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class CommentModel(Document):
    meta = {"collection": "comments"}

    author = ReferenceField(UserModel)
    post = ReferenceField(PostModel)
    content = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class LikeModel(Document):
    meta = {"collection": "likes"}

    user = ReferenceField(UserModel)
    likeable_id = ObjectIdField()
    likeable_type = StringField()
