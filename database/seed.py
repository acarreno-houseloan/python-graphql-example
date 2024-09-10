import argparse
import os

from mongoengine import connect

if __name__ == "__main__":
    DATABASE_URL = os.environ["DATABASE_URL"]
    print(f"Connecting to database at {DATABASE_URL}")
    connection = connect(host=DATABASE_URL)

    # Imports are done here because factory boy runs the query to the database
    # at import time
    from .factories import CommentFactory
    from .factories import PostFactory
    from .factories import UserFactory

    args = argparse.ArgumentParser()
    args.add_argument("--users", type=int, default=10)
    args.add_argument("--posts", type=int, default=20)
    args.add_argument("--comments", type=int, default=50)
    args = args.parse_args()

    UserFactory.create_batch(args.users)
    PostFactory.create_batch(args.posts)
    CommentFactory.create_batch(args.comments)
