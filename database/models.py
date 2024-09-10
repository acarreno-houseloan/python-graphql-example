from datetime import datetime

from mongoengine import Document
from mongoengine.fields import DateTimeField
from mongoengine.fields import ObjectIdField
from mongoengine.fields import ReferenceField
from mongoengine.fields import StringField


class User(Document):
    meta = {"collection": "users"}

    username = StringField()
    email = StringField()
    password = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def __repr__(self):
        return self.username


class Post(Document):
    meta = {"collection": "posts"}

    author = ReferenceField(User)
    title = StringField()
    content = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class Comment(Document):
    meta = {"collection": "comments"}

    author = ReferenceField(User)
    post = ReferenceField(Post)
    content = StringField()
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)


class Like(Document):
    meta = {"collection": "likes"}

    user = ReferenceField(User)
    likeable_id = ObjectIdField()
    likeable_type = StringField()
